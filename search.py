#!/usr/bin/env python3
import csv
import re

file = "countries.csv"

#Extract information from the file
def extract_info(file):
    country_list = []
    with open(file) as f:
        countries = csv.reader(f)
        for row in countries:
            country_list.append(row)

        country_list.pop(0) #removes the headers

        for country in country_list: #reverses the lists, so that the country becomes the key
            country.reverse()

        country_dictionary = dict(country_list)
        return country_dictionary

def search_country():
    user_input = input("Search for a country: ")
    countries = extract_info(file)
    new_list = ""

    #Allows the user to search by continent instead.
    for country in countries:
        continent = countries.get(country)
        if user_input.upper() == continent.upper():
            new_list += str(country) + ", "

        #Uses regex to allow the user to search for a country without spelling the entire word
        search = re.search(user_input.capitalize(), country)
        if search != None:
            result = f"{country} is in {continent}"
            print(result)

    if len(new_list) != 0:
        print(f"Countries in {user_input} are: \n {new_list}")

search_country()

