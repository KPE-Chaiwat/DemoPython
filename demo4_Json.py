import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
z = '{ "name":"kuyparin", "age":30, "city":"KKU"}'
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(json.loads(z))