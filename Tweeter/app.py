from flask import Flask, g, render_template, flash, redirect, url_for #g means global. makes it exist everywhere in the entire app.
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import models #when we import, we will access to class User and initialize. can use models.user and model.initialize
import forms
app = Flask(__name__)
# sets up session secret key for our cookie
app.secret_key = 'sjdflkjflkdkslfjsdlkfaajslkfsdklfsjdflsdfl'


# login Manager sets up our session for us
login_manager = LoginManager()
##attach it to our app
login_manager.init_app(app)
##set up default login view. will be helpful for errors.
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

##manage pool connections to the database
@app.before_request # before ANY requests are made, do this function
def before_request():
    #want to connect to database before each request
    g.db = models.DATABASE #anywhere in our app, can connect to database with g.db
    g.db.connect()
    g.user = current_user
@app.after_request
def after_request(response): #this is the response back to the client.
    #want to close the database after each request
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST')) # accepts both GET or POST
def register():
    global form
    form = forms.RegisterForm()
    ## if statement handling the post request
    if form.validate_on_submit():
        #true or false
        flash('Registration successful', 'success')
        models.User.create_user(
            username=form.username.data, #property in forms.py,    #want req.body like in nodejs
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
# response for the GET request
    return (render_template('register.html' ,form=form))


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("your email or password doesn't match", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                ## creates session
                login_user(user)
                flash("You've been logged in", "success")
                return redirect(url_for('index'))
            else:
                flash("your email or password doesn't match", "error")
    return render_template('login.html', form=form)
    
@app.route('/stream')
@app.route('/stream/<username>')
def stream(username=None):
    template = 'stream.html'
    if username and username != current_user.username:
        user = models.User.select().where(models.User.username**username).get()
        stream = user.posts.limit(100)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'user_profile.html'
    return render_template(template, stream=stream, user=user)    

@app.route('/')
def index():
    ## grab all posts and display them
    stream = models.Post.select().limit(20)
    return render_template('stream.html', stream=stream)

@app.route('/new_post', methods=("GET", "POST"))
@login_required
def post():
    form = forms.postForm()
    if form.validate_on_submit():
        models.Post.create(user=g.user._get_current_object(),                           content=form.content.data.strip()) #.strip() is like like .trim() in javascrtip, cutting out all white spaces
        flash('Messages posted', 'success')
        return redirect(url_for('index'))
    return render_template('posts.html', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    models.initialize() ##seting up our tables.
    try:
        models.User.create_user(
            username='abe',
            email='abe@abe.com',
            password='123456',
            admin=True
        )
    except ValueError:
        pass #pass is do nothing. user was created, then do nothing
    app.run(debug=True, port=8000)
