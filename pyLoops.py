## WhileLoop
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
