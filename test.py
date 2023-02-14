import json as js

filepath ="properties.json"

with open(filepath) as json_file:
    jsstring = js.load(json_file)

json_string = js.dumps(jsstring)
print(jsstring)
exit()
with open('properties.json', 'w') as outfile:
    outfile.write(js.dumps(json_string, indent=4))