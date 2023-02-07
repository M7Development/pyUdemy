# WhileLoop
spam = 0
while spam < 5:
    print('Hello World')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name')
    name = input()

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

## ForLoop
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

print('-------------------------------- Gaus --------------------------')
sum = 0
for i in range(101):
    sum=i+sum
print('Das Ergebnis ist ' + str(sum))


for i in range(12,16):      # Loop startet beu 12 und geht bis 15
    print('How often: ' + str(i))

for i in range(0, 20, 2):      # Loop steigt immer um 2
    print('How often: ' + str(i))
