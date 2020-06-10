from string import ascii_lowercase
"""
This program uses the associated files
    -TownsWithLetterAsPercentageOfAllTowns.txt 
        -contains data pertaining to all 50 states for each letter in the alphabet
        where each number is the percentage of towns in that state that begin with that letter
    -TownsWithLEtterPerMillionPeople.txt
        -contains data pertaining to all 50 states for each letter in the alphabet
        where each number is the number of towns that begin with that letter per million people

    Each file begin with the first state alphabetically (Alabama)
    and the first letter of the alphabet (a) and proceeds
    down the alpabet (a-z) with newlines deliminating data for 
    that state before repeating the process with the next one
"""


states = [
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming",
]

f1 = open("TownsWithLetterAsPercentageOfAllTowns", "r")
f2 = open("TownsWithLEtterPerMillionPeople", "r")

"""
[letterCount] Counts the number of lines read, when it reaches 26, data pertaining
to the current state must have gone a-z
"""
letterCount = 0 
townsAsPercentageOfTowns = [[]] # 2D list, rows correspond to states and colums correspond to letters a-z
townsPerMillionPeople = [[]] # 2D list, rows correspond to states and colums correspond to letters a-z

currentState = [] # Will hold the values corresponding to a-z for the current state

for line in f1: # Reads and appends the data for all states for percentage of towns starting with a given letter
    currentState.append(line[:-1]) # Takes the data from the line but chops off the ending newline character
    count += 1
    if(count == 26):
        townsAsPercentageOfTowns.append(currentState)
        currentState = []
        count = 0

currentState = []

for line in f2: # Reads and appends the data for all states for the number of towns per million people that start with a given letter
    currentState.append(line[:-1])
    count += 1
    if(count == 26):
        townsPerMillionPeople.append(currentState)
        currentState = []
        count = 0

def getMaxBoth():
    """Fetches the maximum values for
        1) The starting letter and the state it is in for the highest percentage of towns that start with that letter in the U.S
        2) The starting letter and the state it is in for the highest number of towns that start with that letter per million people

    Args:
        NONE
    Returns:
        void
    """
    max = 0
    for i in range(0, len(townsAsPercentageOfTowns)):
        for j in range(0, 26): # 26 for the number of letters in the alphabet
            if(float(townsAsPercentageOfTowns[i][j]) > max):
                max = float(townsAsPercentageOfTowns[i][j])
                state = states[i]
                letter = ascii_lowercase[j]
    print("Max town letter as percentage of other towns is " + str(letter) + " in " + str(state))
    max = 0
    for i in range(0, len(townsPerMillionPeople)):
        for j in range(0, 26):
            if(float(townsPerMillionPeople[i][j]) > max):
                max = float(townsPerMillionPeople[i][j])
                state = states[i]
                letter = ascii_lowercase[j]
    print("Max town letter per million people is " + str(letter) + " in " + str(state))

def getFromStateLetter(state: str, letter: str):
    """Prints the following data for a given state and letter
        1) The percentage of towns in that state that begin with that letter
        2) The number of towns in that state that begin with that letter per million people

    Args:
        stateName: the string of the state in question
        letter: the string of the starting town letter
    Returns:
        void
    """

    localStates = [x.lower() for x in states]
    stateIndex = localStates.index(state.lower())
    letterIndex = ascii_lowercase.index(letter.lower())
    print()
    print("The percentage of towns that start with " + str(letter) + " per total towns in " + str(state) + " is " + str(townsAsPercentageOfTowns[stateIndex][letterIndex]))
    print("The number of towns that start with " + str(letter) + " per million people in " + str(state) + " is " + str(townsPerMillionPeople[stateIndex][letterIndex]))

#Example function calls for this program
getMaxBoth()
getFromStateLetter("Illinois", "m")
getFromStateLetter("Wisconsin", "m")
getFromStateLetter("New Jersey", "m")
getFromStateLetter("Oklahoma", "m")
getFromStateLetter("Indiana", "m")