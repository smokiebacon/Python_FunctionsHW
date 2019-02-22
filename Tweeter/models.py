import datetime
from peewee import * #import EVERYTHING from peewee
#peewee is an ORM, like mongoose. talks to database for us
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

#when uppercase, telling other Pythoners is constant. dont change it.
DATABASE = SqliteDatabase('twitclone.db') #real world we'd use PostgresQL or MySQL
'''
UserMixin is a small class from the flask-login. gives User class some special features, create id,
  createing 
 login manager, set up our sessions and load our users. find out if user is authenticated, logout, etc. give our model properties and methods
 '''
class User(UserMixin, Model): #all our models will inherit from Model class. able to set up schema. this is like new Mongoose.Schema
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(unique=True, max_length=70)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)
    # peewee with flask documentation is why we're using CHarField... etc
    class Meta:
        database = DATABASE #setting a variable to connect
    
    def get_posts(self):
        return Post.select().where(Post.user == self)
    
    def get_stream(self):
        return Post.select().where((Post.user == self))

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username, #getting props from the fields on class itself
                email=email,
                password=generate_password_hash(password),
                is_admin=admin #pass admin if we want, if we dont, admin defaults to False
            )
        except IntegrityError:
            raise ValueError("User already exists.")
            # like res.send(errors)
    #try, except same as try, catch in nodejs.

class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
        model=User,
        backref='posts'
    )
    content = TextField()
    class Meta:
        database = DATABASE
        order_by = ('-timestamp',) #comma becuase it makes it a tuple. immutable list.

## express db.js connecting and creating our tables
def initialize():
    DATABASE.connect() #openining connection to our database
    DATABASE.create_tables([User, Post], safe=True) #safe is saying, if this table exists, dont make another table
    DATABASE.close() 