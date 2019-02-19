from random import shuffle

right = 0
wrong = 0
state_capitals={"Washington":"Olympia","Oregon":"Salem",\
                    "California":"Sacramento","Ohio":"Columbus",\
                    "Nebraska":"Lincoln","Colorado":"Denver",\
                    "Michigan":"Lansing","Massachusetts":"Boston",\
                    "Florida":"Tallahassee","Texas":"Austin",\
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                    "Alaska":"Juneau","Utah":"Salt Lake City",\
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                    "South Dakota":"Pierre","West Virginia":"Charleston",\
                    "Virginia":"Richmond","New Jersey":"Trenton",\
                    "Minnesota":"Saint Paul","Illinois":"Springfield",\
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                    "Tennessee":"Nashville","Georgia":"Atlanta",\
                    "Alabama":"Montgomery","Mississippi":"Jackson",\
                    "North Carolina":"Raleigh","South Carolina":"Columbia",\
                    "Maine":"Augusta","Vermont":"Montpelier",\
                    "New Hampshire":"Concord","Connecticut":"Hartford",\
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                    "Montana":"Helena","Kansas":"Topeka",\
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                    "Maryland":"Annapolis","Missouri":"Jefferson City",\
                    "Arizona":"Phoenix","Nevada":"Carson City",\
                    "New York":"Albany","Wisconsin":"Madison",\
                    "Delaware":"Dover","Idaho":"Boise",\
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

shuffle(state_capitals)
for key, val in state_capitals.items():
    state = input(f'What is the capital of {key}? ')
    if state.lower() == val.lower():     
        right = right + 1
        print(val, 'is correct!')
        print(right, 'is the current number of correct guesses.')
    else:
        wrong = wrong + 1  
        print(wrong,'wrong!')
        print(val, 'was the right answer')

print('Thanks for playing!')
print('Total correct: ', right)
print('Total wrong: ', wrong)
