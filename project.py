# GUESS THE NUMBER GAME

import random

target=random.randint(1,100)

while True:
    userchoice=int(input("guess the target:"))
    if(userchoice=="quit"):
        break

    if (userchoice==target):
        print("your guess was correct","\n","YOU WON")
        break

    elif (userchoice<target):
        print("your number is smaller than the target.guess higher number")

    else:
        print("your number is greater than the target.guess smaller number")

print("----GAME OVER----")



# RANDOM PASSWORD GENERATOR

# import random
# import string
# pass_len=12
# charvalues=string.ascii_letters+string.digits+string.punctuation
# password=""
# for i in range(pass_len):
#     password+=random.choice(charvalues)
# print("your random password is:",password)
#   OR
# import random
# import string
# pass_len=12
# charvalues=string.ascii_letters+string.digits+string.punctuation
# password="".join([random.choice(charvalues) for i in range(pass_len)])

# print("your random password is:",password)