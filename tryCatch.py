def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: You tried to diviede by zero.")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("Thats alot!")
    else:
        print("that is not so many")
except ValueError:
    print("you did not entered a number")
except AssertionError:
    print("number is negative")  # it's not working
