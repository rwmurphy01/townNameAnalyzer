# townNameAnalyzer 
Two .py files are provided. `townsAndCities.py` and `townsAndCitiesAnalyzer.py`. Two text files are also provided `TownsWithLetterPerMillionPeople.txt` and `TownsWithLetterAsPercentageOfAllTowns.txt`.

---
### Overview
This repo includes modules that implement python `requests` from demographics.com and analyzes the resulting response with `BeautifulSoup`. Demographics.com provides the following information
* How many towns start with a given letter in a given state
* The total number of towns in a given state
* The population of a given state

The programs calculate and manipulate the following two results
* The percentage of towns in a given state that start with a given letter
* The number of towns that start with a given letter per million people in a given state

`townsAndCities.py` provides functions to create these results by parsing pages from demographics.com. This module can provide results for one state and one letter or for all states and all letters. 
`townsAndCitiesAnalyzer.py` proides functions for analyzing the results and requesting results for one state and one letter in a much faster fasion than `townsAndCities.py` can provide.

---
### townsAndCities.py Usage (Windows commands)
Use this module to caculate the two results from demographics.com. 
1. Make sure you have at least Python 3.7 and the latest version of pip
1. Clone this repository to your machine
1. Create a virtual enviroment `py -m venv env`
1. Start the virtual enviroment `.\env\Scripts\activate`
1. Install requests `pip install requests`
2. Install Beautfiul Soup `pip install bs4`
1. Run the program `py townsAndCities.py`
1. Select which option to run (type `all` or `one`)
    1. `all` will calculate the results for all 50 states and 26 letters, creating the text files provided in the repo again
    1. `one` will provide you the option to specify a state and letter, calculating the results for that state and letter

---
### townsAndCitiesAnalyzer.py Usage (Windows commands)
Use this module to quickly find the results for a specific state and letter as well as calculating the max value for both results across all 50 states.
1. Follow steps 1 -> 2 from above
1. At the bottom of `townsAndCitiesAnalyzer.py` change/append the function calls to suit your needs
    1. `getFromStateLetter(string, string)` takes two arguments and prints the two calculated results based on those arguments
    1. The first argument is the string of the state
    1. The second argument is the string of letter the results are to be calculated for
    1. The program will print the percentage of towns in that state that start with that letter and the number of towns that start with that letter per million people in that state
    1. `getMaxBoth` will print the maximum values for both of the results across all 50 states. Delete this function call if you do not have need for this information.
1. Run the program `py townsAndCitiesAnalyzer.py`
