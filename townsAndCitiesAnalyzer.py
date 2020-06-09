from string import ascii_lowercase

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

count = 0
townsAsPercentageOfTowns = []
townsPerMillionPeople = []

currentState = []

for line in f1:
    currentState.append(line[:-1])
    count += 1
    if(count == 26):
        townsAsPercentageOfTowns.append(currentState)
        currentState = []
        count = 0

currentState = []

for line in f2:
    currentState.append(line[:-1])
    count += 1
    if(count == 26):
        townsPerMillionPeople.append(currentState)
        currentState = []
        count = 0

def getMaxBoth():
    max = 0
    for i in range(0, len(townsAsPercentageOfTowns)):
        for j in range(0, 26):
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

def getFromStateLetter(state, letter):
    localStates = [x.lower() for x in states]
    stateIndex = localStates.index(state.lower())
    letterIndex = ascii_lowercase.index(letter.lower())
    print()
    print("The percentage of towns that start with " + str(letter) + " per total towns in " + str(state) + " is " + str(townsAsPercentageOfTowns[stateIndex][letterIndex]))
    print("The number of towns that start with " + str(letter) + " per million people in " + str(state) + " is " + str(townsPerMillionPeople[stateIndex][letterIndex]))

getMaxBoth()
getFromStateLetter("Illinois", "m")
getFromStateLetter("Wisconsin", "m")
getFromStateLetter("New Jersey", "m")
getFromStateLetter("Oklahoma", "m")
getFromStateLetter("Indiana", "m")