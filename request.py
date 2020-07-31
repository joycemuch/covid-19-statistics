import requests




total_cases = requests.get("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
total_deaths= requests.get("https://covid.ourworldindata.org/data/ecdc/total_deaths.csv")
new_cases= requests.get("https://covid.ourworldindata.org/data/ecdc/new_cases.csv")
new_deaths= requests.get("https://covid.ourworldindata.org/data/ecdc/new_deaths.csv")




open("Data/total_cases.csv"    , "wb").write(total_cases.content )
open("Data/total_deaths.csv"    , "wb").write(total_deaths.content )
open("Data/new_cases.csv"    , "wb").write(new_cases.content )
open("Data/new_deaths.csv"    , "wb").write(new_deaths.content )

total_cases ="Data/total_cases.csv"
total_deaths = "Data/total_deaths.csv"
new_cases="Data/new_cases.csv"
new_deaths="Data/new_deaths.csv" 