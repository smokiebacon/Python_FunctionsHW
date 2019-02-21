colors = ['red', 'green', 'blue'] 
len(colors)
print(colors)
colors[-1] # => blue (backwards)
colors[-1] = 'baby blue'   #now becomes [red, green, baby blue]

#adding elements
#adding a SINGLE element
colors.append('purple')
#adding multi elements, use extend()
colors.extend(['orange', 'black'])


#Inserting Elements

colors.insert(1, 'yellow') #inserts at index 1
['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']



#deleting colors at index 1
del colors[1]
colors.remove('red')
print(colors)
#colors.clear() # clears out the array. returns emtpy array


#iteration
for color in colors:
    print(color)

#lets say we need index number
for index, color in enumerate(colors):
    print(index, color)
#  > 0 red
#  > 1 green
#  > 2 blue

nums = [1,2,3,4,5,6,7,8,9]
#Let's square all the numbers
squares = []
for n in nums:
    squares.append(n * n)
print(squares


)


#List Comprehension example
# [<expression> for <item> in <list>]
# popular way to do it
squares = [n * n for n in nums] # n is just an var name
squares = [turkey * turkey for turkey in nums] 

# List Comprehension: Filter for even squares
nums = [1,2,3,4,5,6,7,8,9, 10]
even_squares []
for n in nums:
    square = n * n
    if square % 2 == 0:
        even.squares.append(square)
print(even_squares)

# Pythonic way. thiis is the way to do it in the real world.
even_squares = [n * n for n in nums if (n * n) % 2 == 0]
                       #parenthasis around (n*n) bc order of operations matter. want to n^2 before modding


# Tuples
#Tuples in Python are very similar to lists.
#Tuples have a class (type) of tuple.
#we can think of tuples as IMMUTABLE! lists. in parentheses
colors = ('red', 'green', 'blue')
colors = 'red', 'green', 'blue'
#tuple as well becuase of the COMMAS! commas make it tuple

 #Find the type of something
 #in javascript, we have typeof
 #Python, it is just type
 print(type(colors)) # => tuple

#However, creating single-item tuples without parens requires a trailing comma:

 colors = 'purple',  # tuple, not a string!
 print(type(colors), len(colors))
#  > <class 'tuple'> 1
#  print(colors)
#  > ('purple',)
green_index = colors.index('green')
print(green_index) # => 1

for index, color in enumerate(colors):
    print(index, color)
# > 0 red
 # 1 green
 # 2 blue

#Tuples have a convenient feature, called unpacking, for doing multiple variable assignment:
#destructered in JS

colors = 'red', 'green', 'orange' 
#vars that are being assigned to the corresponding index
red, green, orange = colors #not changing the original tuple
red = 'orangered' #will print orangered
print(red, green, orange)

#in JS
#const arr = [1,2,3]
### [one, two, three] = arr




### Ranges
#Ranges have a class type of range
#range type represents an immutable sequence of numbers, and their usuaully used 
# with a lop to iteratue a certain number of times

for num in range(5): #remember, not inclusive. won't print 5
    print(num)
#  > 0
#  > 1
#  > 2
#  > 3
#  > 4


#first args is starting point, 2nd is end point, 3rd point is step
#loop from 2 to 10, incrementing by 2
for even in range(2, 10, 2):
    print(even)
    # => 2, 4, 6, 8

nums_thru_nine = list(range(10))
print(nums_thru_nine) # => 0-9
# > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = tuple(range(1, 10, 2))
print(odds)
# > (1, 3, 5, 7, 9)


# Can count down in Range as well
#start at 5, want to end at 0. decrement by 1
for num in range(5, 0, -1):
 	print(num)
#  > 5
#  > 4
#  > 3
#  > 2
#  > 1

###Slicing Sequences
#start from 0 index up to 4th index. end point is NOT inclusive.
short_name = "Alexander"[0:4]
print(short_name) # => Alex


colors = ('red', 'green' 'blue')
print(colors[:2])  ##if we omit first arg, sequence starts copying at the beginning
# => red, green
#If 2nd arg is omitted, the slice copies the sequence all the way to the end:
print(colors[1:]) # => green, blue

fruit = ('apples', 'bananas', 'oranges')
fruit_copy = fruit[:]
print(fruit_copy) # => apples, bananas, oranges. makes a copy of the tuple

