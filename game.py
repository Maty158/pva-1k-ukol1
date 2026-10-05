import random as r

secret = r.randint(1, 100)
attempts = 0

while True:
    guess = input("I'm thinking of a number between 1 and 100: ")

    try:
        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Your guess is out of range.")
            continue

        attempts += 1

        if guess > secret:
            print("Your guess is too high, close!")
        elif guess < secret:
            print("Your guess is too low, too bad!")
        else:
            print("You got it!!!")
            print("It took you", attempts, "tries.")
            break

    except ValueError:
        print("Couldn't read that, try typing in a number.")
