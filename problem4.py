cities = {"Boston": 0,
          "New York": 0,
          "Vienna": 0,
          "Sofia": 0}
user_input = input()
city_values = {}
values = 0
while user_input in cities.keys():
    cities[f"{user_input}"] = input()
    values = cities[user_input]
    city_values[f"{user_input}"] = f"{values}"
    print(user_input, cities[user_input])
    values = 0
    user_input = input()
else:
    for key in city_values.keys():
        print(key, city_values[key])
