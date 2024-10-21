import json 

from country_codes import get_country_codes

#load data into a list 
filename = "./world_population.json"
with open(filename) as fn:
    #makes the data into a python list of dict Ks:country, population
    pop_data = json.load(fn)

country_codes, population = [], []

# print the 2010 population for each country 
for data_point in pop_data:
    country_name = data_point["country"]
    country_code = get_country_codes(country_name)

    try: 
        country_population = int(data_point["population"])
        
    except ValueError:
            print(country_population, "Missing data point")

    if country_codes:
        country_codes.append()
        population.append(country_population)
    else: 
         continue