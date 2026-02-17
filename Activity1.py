import random
x = True
number = random.randint(0, 10)

print("I will get a number 0 to 10, and you have to guess the number one at a time. You win when you get one hero")

while x:
    attempt = int(input("Guess: "))
    if number == attempt:
        print("You won")
        break
    else:
        print("Not correct")