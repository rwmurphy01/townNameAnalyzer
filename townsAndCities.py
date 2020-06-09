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
]
newStates = [
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

def getNumTownsWithLetter(stateName, letter):
    url = "https://www." + stateName.lower() + "-demographics.com/counties-cities-that-begin-with-" + letter.upper()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    hOneTags = soup.findAll("h1")
    for tag in hOneTags:
        if("No City" in tag.text):
            return 0
    
    firstSpanSix = soup.findAll("div", {"class": "span6"})
    aTags = firstSpanSix[1].findAll("a")
    return len(aTags)


def getTotalTowns(stateName):
    url = "https://www." + stateName.lower() + "-demographics.com/cities_by_population"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('p')

    for p in results:
        if("Below are " in p.text):
            index = p.text.find("Below are ")
            index = index + 10
            nextSpace = p.text.find(" ", index)
            return p.text[index: nextSpace]

def getPopulation(stateName):
    url = "https://www." + stateName.lower() + "-demographics.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('li')

    for li in results:
        if("population" in li.text):
            index = li.text.find("population")
            nextSpace = li.text.find(" ", index + 14)
            return li.text[index + 14: nextSpace]

def runAllStatesAllLetters(): 

    f1 = open("TownsWithLetterAsPercentageOfAllTowns", "a")
    f2 = open("TownsWithLEtterPerMillionPeople", "a")

    for state in newStates:   
        state = state.replace(" ", "")
        print(state)
        stateDataTowns = []
        stateDataPop = []
        for c in ascii_lowercase:
            print(c)
            numTowns = getNumTownsWithLetter(state, c)
            totalTowns = getTotalTowns(state)
            population = getPopulation(state)

            population = population.replace(",", "")
            population = float(population) / 1000000

            townsWithLetterPerTowns = (float(numTowns) / float(totalTowns)) * 100
            townsWithLetterPerPop = float(numTowns) / float(population)
            f1.write("%s\n" % townsWithLetterPerTowns)
            f2.write("%s\n" % townsWithLetterPerPop)
        print("State " + state)
        print("DONE!")

    print("DONE")
    print("DONE")
    print("DONE")
    f1.close()
    f2.close()

def runForOneStateOneLetter():
    stateName = input("What state? ")
    letter = input("What letter? ")
    stateName = stateName.replace(" ", "")

    numTowns = getNumTownsWithLetter(stateName, letter)
    totalTowns = getTotalTowns(stateName)
    population = getPopulation(stateName)

    population = population.replace(",", "")
    population = float(population) / 1000000

    townsWithLetterPerTowns = float(numTowns) / float(totalTowns)
    townsWithLetterPerPop = float(numTowns) / float(population)


    print("Total number of towns with the letter " + letter + " in " + stateName + " is " + str(numTowns))
    print("Total number of towns in " + stateName + " is " + totalTowns)
    print("The population of " + stateName + " is " + str(population) + " million")
    print("The percentage of towns with that letter per total towns is " + str(round(townsWithLetterPerTowns * 100, 3)))
    print("The number of towns with that letter per million people is " + str(townsWithLetterPerPop))

print("Do you want to run program to generate data for all states and letters or just one state and one letter?")
whichFunction = input("(please enter \"all\" or \"one\"): ")
if(whichFunction.lower() == "all"):
    runAllStatesAllLetters()
else:
    runForOneStateOneLetter()


