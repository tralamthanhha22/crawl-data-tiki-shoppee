import json
f = open('tiki.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['long_description']:
    print(i)
 
# Closing file
f.close()