# python variable names are snack_case
#no semi-colons, indent matters
first_name = "Jim"
x = 2 # just like let in javascript
x = 9

###since there is no CONST, we make the variable name in ALL CAPS
NUMBER_OF_DAYS = 7 #lets other pythoners this var shouldn't be changed
#however, it is changeable if we reassign them, wont throw error. dont change it tho

### Falsy Values
False
None ## null in javascript
0 #integers
0.0 #floats
###

'' # string, doesnt matter if single or double quotes.'', or ""
[] # list. (arrays)
{} # dictionary. (objects)

# in javascript &&, ||, !
# python literally the word itself: and, or, not
# math: in python, +, -, *, /, //, %
# double division is float. rounds it DOWN!
14.5 / 3 # => 4.8333
14.5 // 3 # => 4, double division rounds it DOWN

int(12.4) # => 12

float(14) # => 14.0


# string interpolation
thing_to_do = "buy milk"
way_to_do_it = "at the store"
person = "Amber"

"{}{}{}. But {}!".format(thing_to_do, way_to_do_it,pronoun) 


# Flow Control
# indention matters! 
if x < 0:
    print('Negative') # like console.log
elif x == 0: # else if in javascript
    print('Zero')
else:  
    print('Positive')


# for loops, while
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count, "is not less than 5") # else is optional!!!!


count = 15
for i in range(1, count): # range can take 2 params, starting point and ending point
    print(i)    #is inclusive. includes the number 15.

# Functions
def function_example(param_one, param_two):
    """ triple quotes. must have explicit return. this is a docString and can be used to leave documentation 
    throughout the codebase"""
    return param_two # MUST RETURN SOMETHING!

function_example('something', 4)  #invoking the function

#lists are like arrays in javascript
secret_files = ["Top Secret", "Also super secret!"]
new_secrets = ["can you keep a secret?", "simple and clean"]

#can add both arrays together. concat them together
secret_files = secret_files + new_secrets

#how to get .length?
len(secret_files)  #returns length of array

#instead of .push, pythn has .append
secret_files.append('ultra FBI secret!')

# .pop() removes last element
secret_files.pop()

secret_files.remove(0) # .remove() takes in some # index and rmeoves that index
#will remove the 0 (first index)

#looping through a list
for file in secret_files: #file is variable name we want to name the var in array list
    print(file)




### Dictionaries. (Objects) #keys must be strings.
#in comp sci, may hear the as maps or associative arrays
student = {
    'name': 'abe',
    'course' : 'WDI',
    'lunch' : 'taco',
    'day' : 30,
    'in_my_wallet': ['coins', 'dollars', 'tissues']
}

#Tuples are lists that CAN'T be changed
# Getting and Setting Values
print(student['name']) # => abe

#setting a name. mutable. we just reassigned name
student['name'] = 'sophia'

#what if i grab key that's not there?
print(student['age']) #python will yell at you. key error. age is not defined

## can use the get method to retrieve properties
print(student.get['age']) # => none (null)
print(student.get['day']) # => 30

#set a value if none exists, but doesn't actually ADD THE ojbect itself
student.get('birthdate', '6/29/1992')
student['birthdate'] = '6/29/1992'  # actually ADDS and sets to the object'

#can add properties on the fly like javascript
student['hungry'] = True

#delete keys
del student['hungry']

# check if keys exists
'hungry' in student # => False (because we just deleted it)

# .length in JS
len(student) # => find out how many keys in the dictionary


# best practice to iterate over dict.
print(student.items()) # => prints entire dictionary. .items is a python method.
#it is a Tuple, which are IMMUTABLE list.
for key, val in student.items():
    print(f"{key} = {val}")  # another way to do string interpolation

