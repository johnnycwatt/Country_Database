#!/usr/bin/env python3
import csv

def extract_file(file):
    with open(file) as f:
        country_list = []
        countries = csv.reader(f)
        for row in countries:
            row.pop(1)
            country_list.append(row)

        country_list.pop(0)
        return country_list


def get_user_year():
    user_year = input("Choose a year in between 1960 and 2016: ")


    try:
        user_year = int(user_year)
    except:
        print("You didn't choose a number!")
        return



    while user_year > 2016 or user_year < 1960: #If year is outside of range, will ask for user input again.
        user_year = input("Sorry we don't have information for that year.\nPlease choose a year between 1960 - 2016: ")
        try:
            user_year = int(user_year)
        except:
            print("You didn't choose and number!")
            return None

    year = user_year - 1959
    return year


def get_population(user,year):
    file = "population_data.csv"
    country_list = extract_file(file)


    for country in country_list:
        try:
            if user in country[0]:
                result = country.pop(year)
                result = int(result)
                return result

        except:
            result = None
            return result



