dict_one = {"a": 1,
            "b": 2,
            "c": 3}
dict_two = {"a": 1,
            "b": 2,
            "d": 3}
k = []
k2 = []
diff = []
dict_three = {}
for i in dict_one.keys():
    k.append(i)
for i in dict_two.keys():
    k2.append(i)
for d in k[:]:
    if d != k2[:]:
        diff.append(d)

print(diff)