#!/usr/bin/env python3
import csv
import re


#Extract information from the file
def extract_info():
    file = "countries.csv"
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

def search_continent():
    from population import get_population
    from population import get_user_year

    user_input = input("Search for a country: ")
    countries = extract_info()
    new_list = []
    year = get_user_year()
    is_continent = False

    #Allows the user to search the total population of the world
    if user_input.upper() == "WORLD":
        people = get_population("World",year)
        print(f"There were {people:,} in the World in {year + 1959}")

    #Allows the user to search by continent instead.
    for country in countries:
        continent = countries.get(country)
        if user_input.upper() == continent.upper():
            new_list.append(country)
            is_continent = True


        if " " in user_input.strip(): #If User searches for a country with two words eg. "United States" "New Zealand"
            search = re.search(user_input, country)
        else:
            #Uses regex to allow the user to search for a country without spelling the entire word. eg. every country starting with A
            search = re.search(user_input.capitalize(), country)

        if search != None:
            people = get_population(country, year)
            if people != None:
                result = f"\n{country} is in {continent}.\nThere were {people:,} in {country} in the year {year + 1959}"
                print(result)

            else:
                print(f"\n{country} is in {continent}.\nUnfortunately we don't have any information about the population in the year you chose.\n")

    #Checks if the user_input was a Continent
    if is_continent == True:
        total = 0
        total_country = f"The countries in {user_input} are: "
        for country in new_list:
            people = get_population(country, year)
            total_country += country + ", "
            if people != None:
                total += int(people)


        print(total_country)
        print(f"There were {total:,} in {user_input} in the year {year + 1959}")

user_input = "YES"
while user_input.upper() != "NO":
    if user_input.upper() == "YES":
        search_continent()
        user_input = input("\nWould you like to make another search? ")
    else:
        user_input = input("Invalid choice. Please try again.\nWould you like to make another search? ")


print("Bye Bye! :)")

