import random as r

secret = r.randint(1, 20)
guess = int(input("Im thinking of a number between 1 and 20: "))

if guess < 1 or guess > 20:
    print("Your guess is out of range: " )
elif guess > secret:
    print("Your guess is too high, close!: " )
elif guess < secret:
    print("Your guess is too low, too bad: ")
else:
    print("You got it!!!: ")
