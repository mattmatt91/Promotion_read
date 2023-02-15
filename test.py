import json as js

filepath ="properties.json"

with open(filepath) as json_file:
    jsstring = js.load(json_file)

json_string = js.dumps(jsstring, indent=3)
print(json_string)
with open('properties.json', 'w') as outfile:
    outfile.write(json_string)