numbers_1 = {0: 'Zero',
             1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: 'Five',
             6: 'Six',
             7: 'Seven',
             8: 'Eight',
             9: 'Nine',
             10: 'Ten',
             11: 'Eleven',
             12: 'Twelve',
             13: 'Thirteen',
             14: 'Fourteen',
             15: 'Fifteen',
             16: 'Sixteen',
             17: 'Seventeen',
             18: 'Eighteen',
             19: 'Nineteen',
             20: 'Twenty',
             21: 'Twenty-one',
             22: 'Twenty-two',
             23: 'Twenty-three',
             24: 'Twenty-four',
             25: 'Twenty-five',
             26: 'Twenty-six',
             27: 'Twenty-seven',
             28: 'Twenty-eight',
             29: 'Twenty-nine',
             30: 'Thirty',
             31: 'Thirty-one',
             32: 'Thirty-two',
             33: 'Thirty-three',
             34: 'Thirty-four',
             35: 'Thirty-five',
             36: 'Thirty-six',
             37: 'Thirty-seven',
             38: 'Thirty-eight',
             39: 'Thirty-nine',
             40: 'Forty',
             41: 'Forty-one',
             42: 'Forty-two',
             43: 'Forty-three',
             44: 'Forty-four',
             45: 'Forty-five',
             46: 'Forty-six',
             47: 'Forty-seven',
             48: 'Forty-eight',
             49: 'Forty-nine',
             50: 'Fifty'}

while True:
    try:
        user_input = int(input())
        if 0 < user_input <= 50:
            print(numbers_1.get(user_input))
            break
        elif user_input > 50:
            print("Number is higher than 50")
            continue
        elif user_input < 0:
            print('Number is lower than 0')
            continue
    except ValueError:
        print("Please enter a valid number from 1 to 50")
        continue
