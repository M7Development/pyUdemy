import pyperclip

print('Hello')

print('Goodbye')

i = 'Hello'
# Pyhtonkurs
print(type(i))

type(i)

# Udemy
pyperclip.copy(111)

# pyperclip.copy('Hello!')

spam = str(pyperclip.paste())

print(spam)


def hello():
    print("Howdy!")
    print("Hi!")


hello()
hello()
hello()

def hello(name):
    print("Howdy! "+ name)
    print("Hi!")

hello("Bob")
hello("Nick")


def plusOne(number):
    return number + 1

print(plusOne(5))

print("Cat", "Dog", "Mouse")

print("Cat", "Dog", "Mouse", sep='***')     # nützlich
print("Hello", end='  ')                    # nützlich
print("World")

def example():
    global eggs     #dadurch wir der global gesetze Wert überschireben, sobald die funktion nach der Initialisierung aufgerufen wird
    eggs="Hello"
    print(eggs)

eggs=50
example()
print(eggs)