#!/usr/bin/env python3
import csv

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
    user = input("Choose a country or a continent: ")
    countries = extract_info(file)
    result = ""
    for country in countries:
        continent = countries.get(country)
        if user == continent:
            result += country + ", "
        elif user == country:
            result = continent
        else:
            "Sorry, that was an invalid choice"

    return result


print(search_country())

