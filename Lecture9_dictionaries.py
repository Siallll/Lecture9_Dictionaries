l = ["alpha", "omega", "gamma"]
print(l)
d = {
    1: "alpha",
    2: "omega",
    3: "gamma"
}  # a dictionary on different lines
print(d[1])
print(d)
# Same as lists, variable on left side = {} difference is [] for lists and {} is for dictionaries
# a = { key: Value} this can be on different lines

# print(d[99]) # Invalid key- raises a error
print(d.get(99))  # .get function will not raise error( will return 'None')

try:  # try key to avoid error or find value
    d[99]
except KeyError:
    print("Invalid key")
# .get
print(d.get(2))  # gets from dictionary d if key is not valid will return None
letter = d.get(1)  # get is a secure way to retrieve information
if not letter:  # loop to avoid key error and find value in dictionary
    print('Invalid key')
else:
    print(letter)
car = {'car': 'Audi'}
car['color'] = "Black"  # adding a key and value in the dictionary
print("Model: {} \t Color: {}".format(car['car'], car['color']))

# updating adding
d[4] = "beta"  # adding a key + value to it
print(d)

# del function- to delete a key with value must use try except
try:
    del d[5]
    print(d)
except:
    print("Key does not exist")
old_value = d.pop(4)  # saving value of deleted key to variable and deleting the key
print(d)
print(old_value)  # the saved value of deleted key
# .copy - making deep copy of dictionary

copy_d = d.copy()
print(copy_d)
print(id(d))  # id of original var
print(id(copy_d))  # id of deep copy different from original

car = {"year": 2018}
car1 = car.copy()
car1["year"] = 2019
print(car, car1)
car = {"year": 2018, "color": "blue"}
car1 = sorted(car)  # sorted sorts by default A-Z and 0-inf
print(car1)

d = {
    1: "alpha",
    2: "omega",
    3: "gamma"
}
for key in d.keys():
    print(key)
    print(d[key])  # prints values of keys in dict

print(d.keys())  # prints dict keys

for val in d.values():  # .values returns values of keys in dict
    print(val)

for t in d.items():  # .items
    print(t)  # prints keys and values
