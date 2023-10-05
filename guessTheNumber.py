# This is a guess the number game
import random
print("Hello. What's your name?")
name = input()
defienedNumber = random.randint(1, 20)

print("Well " + name + ", I'm thinking of a number between 1 and 20")

for guessesTaken in range(0, 6):
    print("Take a guess.")
    guess = int(input())
    if guess==guessesTaken :
        print("Congratulations. You are right!")
    elif guess<guessesTaken :
        print("The number should be higher")
    elif guess>guessesTaken :
        print("The number should be lower")


print("You took "+ str(guessesTaken) +" guesses! The number that I had in mind was " + str(defienedNumber))
