menu = {"tea": 1,
        "coffee": 1,
        "croissant": 2,
        "fried bread": 2,
        "pizza": 3}
user_input = input()
total = 0
while user_input != "":
    for d in menu.keys():
        if d == user_input:
            choice_price = menu[d]
            print(f"Order:{d}")
            total += choice_price
            print(f"{d} costs {choice_price} total is:{total}")
    user_input = input()
else:
    print(f"Thank you! Total is:{total}")
if user_input == int:
    print(f"Sorry we dont have {user_input} in the menu")
    user_input = input()