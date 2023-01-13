import math

age = 25
gender = "f"
height = 163
weight = 50
activity_lvl = 2
BMR = 0
if gender == "m":
    bmr = 66.47 + 13.75 * weight + 5.003 * height - 6.755 * age
else:
    bmr = 655.1 + 9.563 * weight + 1.85 * height - 4.676 * age
activity = {1: 1,
            2: 1.2,
            3: 1.375,
            4: 1.55,
            5: 1.725,
            6: 1.9}

while 0 < activity_lvl < 7:
    if activity_lvl == 1 and gender == "m":
        BMR = activity.get(1) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 1 and gender == "f":
        BMR = activity.get(1) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 2 and gender == "m":
        BMR = activity.get(2) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 2 and gender == "f":
        BMR = activity.get(2) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 3 and gender == "m":
        BMR = activity.get(3) * bmr
        print(math.ceil(BMR))
        break
    elif BMR == 3 and gender == "f":
        BMR = activity.get(3) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 4 and gender == "m":
        BMR = activity.get(4) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 4 and gender == "f":
        BMR = activity.get(4) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 5 and gender == "m":
        BMR = activity.get(5) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 5 and gender == "f":
        BMR = activity.get(5) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 6 and gender == "m":
        BMR = activity.get(6) * bmr
        print(math.ceil(BMR))
        break
    elif activity_lvl == 6 and gender == "f":
        BMR = activity.get(6) * bmr
        print(math.ceil(BMR))
        break
lose_half_kg = BMR - 500
lose_one_kg = BMR - 1000
gain_half_kg = BMR + 500
gain_one_kg = BMR + 1000
print(f"Имате нужда от {math.ceil(BMR)} калории на ден за да поддържате теглото си")
print(f"Имате нужда от {math.ceil(lose_half_kg)} калории на ден за да сваляте по 0.5 кг на седмица")
print(f"Имате нужда от {math.ceil(lose_one_kg)} калории на ден за да сваляте по 1 кг на седмица")
print(f"Имате нужда от {math.ceil(gain_half_kg)} калории на ден за да качвате по 0.5 кг на седмица")
print(f"Имате нужда от {math.ceil(gain_one_kg)} калории на ден за да качвате по 1 кг на седмица")

