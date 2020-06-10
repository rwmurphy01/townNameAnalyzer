import requests
from bs4 import BeautifulSoup
import sys
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

def getNumTownsWithLetter(stateName: str, letter:str) -> int:
    """Fetches the number of towns with a certain letter in a given state

    Retrieves the data from demographics.com by parsing their webpage

    Args:
        stateName: the string of the state the town is located in 
        letter: the letter to be counted in the state
    Returns:
        int: The number of towns in "stateName" that start with "letter"
    """

    #There is a webpage for every letter in every state on demographics.com
    url = "https://www." + stateName.lower() + "-demographics.com/counties-cities-that-begin-with-" + letter.upper()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Gets all of the <h1> tags since if and only if no town starts with "letter" one of the <h1> tags will contain "No city"
    hOneTags = soup.findAll("h1") 
    for tag in hOneTags:
        if("No City" in tag.text):
            return 0
    
    #The website includes links for each town that starts with the given "letter" and they are always located in a <div class="span6">
    firstSpanSix = soup.findAll("div", {"class": "span6"})
    aTags = firstSpanSix[1].findAll("a")
    return len(aTags)

def getTotalTowns(stateName: str) -> int:
    """Fetches the total number of towns in a given state

    Retrieves the data from demographics.com by parsing their webpage

    Args:
        stateName: the string of the state the towns are to be counted in
    Returns:
        int: The number of total towns in "stateName"
    """
    url = "https://www." + stateName.lower() + "-demographics.com/cities_by_population"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('p')

    # Always directly following "Below are " in one of the <p> tags on the page is the count of total towns
    for p in results:
        if("Below are " in p.text):
            index = p.text.find("Below are ")
            index = index + 10 #10 spots away from the B in "Below are" is the beginning of the number
            nextSpace = p.text.find(" ", index) #Finds the index relative to the beginning of the number where it ends
            return p.text[index: nextSpace]

def getPopulation(stateName: str) -> int:
    """Fetches the total population of a given state

    Retrieves the data from demographics.com by parsing their webpage

    Args:
        stateName: the string of the state in question
    Returns:
        int: The population of the state
    """

    url = "https://www." + stateName.lower() + "-demographics.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('li')

    # Always in one of the <li> tags on the page is the population of the state
    for li in results:
        if("population" in li.text):
            index = li.text.find("population")
            index = index + 14 # The beginning of the number is always 14 spaces away from the p in "population"
            nextSpace = li.text.find(" ", index) #Locates the end of the number
            return li.text[index: nextSpace]

def runAllStatesAllLetters(): 
    """Prints values for the starting letters of towns for all 50 states to text files

    The function computes the value for each letter in the alphabet:
         1) The number of towns starting with this letter as a percentage of total towns in the state
         2) The number of towns starting with this letter per million residents of the state
    Each of these values is printed to their own text files (2 text files total) 
    where the first 26 results are for the first state alphabetically
    and the second 26 results are for the second state alphabetically and so on.

    Args:
        None
    Returns:
        void
    """
    f1 = open("TownsWithLetterAsPercentageOfAllTowns", "a") #Opens text file for towns with letter as percent of total towns
    f2 = open("TownsWithLEtterPerMillionPeople", "a") # Opens text file for towns with letter per million residents

    for state in newStates:   
        state = state.replace(" ", "")
        print(state) # Prints the state so you can keep track of where the program is at
        stateDataTowns = []
        stateDataPop = []
        for c in ascii_lowercase:
            print(c)
            numTowns = getNumTownsWithLetter(state, c)
            totalTowns = getTotalTowns(state)
            population = getPopulation(state)

            population = population.replace(",", "")
            population = float(population) / 1000000

            townsWithLetterPerTowns = (float(numTowns) / float(totalTowns)) * 100 # This number is a percentage so multiple by 100
            townsWithLetterPerPop = float(numTowns) / float(population)
            f1.write("%s\n" % townsWithLetterPerTowns)
            f2.write("%s\n" % townsWithLetterPerPop)
    f1.close()
    f2.close()

def runForOneStateOneLetter():
    """ Gets user input and calculates the following two values regarding a letter and a state
            1) The percentage of towns in that state that start with the letter
            2) The number of towns per million people that begin with that letter in the given state

    Args:
        NONE
    Returns:
        void
    """

    stateName = input("What state? ")
    letter = input("What letter? ")
    stateName = stateName.replace(" ", "")

    numTowns = getNumTownsWithLetter(stateName, letter)
    totalTowns = getTotalTowns(stateName)
    population = getPopulation(stateName)

    population = population.replace(",", "")
    population = float(population) / 1000000 #Reduces the population to the number of million people

    townsWithLetterPerTowns = (float(numTowns) / float(totalTowns)) * 100 # Percentage, multiply by 100
    townsWithLetterPerPop = float(numTowns) / float(population)


    print("Total number of towns with the letter " + letter + " in " + stateName + " is " + str(numTowns))
    print("Total number of towns in " + stateName + " is " + totalTowns)
    print("The population of " + stateName + " is " + str(population) + " million")
    print("The percentage of towns with that letter per total towns is " + str(round(townsWithLetterPerTowns, 3)))
    print("The number of towns with that letter per million people is " + str(townsWithLetterPerPop))

"""
This program generates the data for one state and one letter or for all states and all letters
    1) The percentage of towns in that state that start with the given letter
    2) The number of towns starting with the given letter per million people in the given state
"""

print("Do you want to run program to generate data for all states and letters or just one state and one letter?")
whichFunction = input("(please enter \"all\" or \"one\"): ")
if(whichFunction.lower() == "all"):
    runAllStatesAllLetters()
else:
    runForOneStateOneLetter()