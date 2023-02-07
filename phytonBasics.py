# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This program says Hello and asks for my name

print('Hello world!')
print('What is your name?')
myName=input()                              # einlesen von einer Eingabe
print('It\'s good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be '+ str(int(myAge)+1) +' in a year.')


print(len('Haus')*10)
print(str(30))
print(int('234'))
print(float('34.34'))
print(float(1))
print('\n \n')
#____________________________________________________________________________________________________ IF ELSE ELIF
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')


pwd = 'swordfish'
if pwd == 'swordfish':
    print('access granted')
else:
    print('Access denied')

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 15:
    print('You are not Alice kid')
elif age > 2000:
    print("Are you a Vampire?")
elif age > 100:
    print('you are not Alice ganny')

print('Enter a name')
name = input()            #If there will be entered something, the statement becomes truthy otherwise it would by falsey
if name:
    print('You entered a Name')
else:
    print('You did not entered a Name')

