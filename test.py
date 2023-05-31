import json as js
import numpy as np

"""
filepath ="properties.json"

with open(filepath) as json_file:
    jsstring = js.load(json_file)

json_string = js.dumps(jsstring, indent=3)
print(json_string)
with open('properties.json', 'w') as outfile:
    outfile.write(json_string)

"""

d = 6
dichte = 8  # g/cm3


m = (dichte * 4/3 * np.pi *np.power(0.5*d, 3))/1000
emax = 0.7*9.81*m
emin = 0.2*9.81*m
print(f'new mass:{m}, Emax:{emax}mJ, Emin{emin}mJ')