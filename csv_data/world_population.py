import json 

import pygal.maps as pm
from pygal.style import RotateStyle as style

from country_codes import get_country_codes

#load data into a list 
filename = "./world_population.json"
with open(filename) as fn:
    #makes the data into a python list of dict Ks:country, population
    pop_data = json.load(fn)

#Build a dict of population data
cc_populations = {}

# print the 2010 population for each country 
for data_point in pop_data:
    country_name = data_point["country"]
    country_code = get_country_codes(country_name)

    try: 
        country_population = int(data_point["population"])
        
    except ValueError:
            print(country_population, "Missing data point")

    if country_code:
        cc_populations[country_code] = country_population

#Group Country into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
          cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else: 
        cc_pops_3[cc] = pop

wm_style = style('#336699')
wm = pm.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')