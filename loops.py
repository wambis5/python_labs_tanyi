#!/home/tanyi/study/CCNA/CCNA_online/1_notes/9-week9/python_labs/ccna_class_labs/usr/bin/python3

text = 'blood-oxygenation level dependent functional magnetic resource imaging'
for i in text:
    print(i)
print()

snack = ['cakes','groundnut','garri', 'nutsweets', 'suggarballs', 'chips']
for i in snack:
    print('Note to self, buy ',i)

print()
for i in range(len(snack)):
    print(i, snack[i])

print()
favoritesnack = 'garri'
for i in snack:
    if favoritesnack not in snack:
        print('warning! no favorate snack')
        break
    
    if i == favoritesnack:
        print('Note to self, buy ',i)
        break
    else: print('Note to self, buy ',i)

print()

print(('hey '*100))

count = 1
while count < 11:
    print(count, favoritesnack)
    count +=1

while count < 11:
    print(count, favoritesnack*count)
    count +=1

copies = ''
while count < 101:
    copies += favoritesnack+' '
    count +=1
print(copies)


while count < 101:
    print(favoritesnack,end=' ')
    count +=1
print()

for i in range(len(snack)):
    print(i, snack[i])

#u still hav e to use enumerate when you a gonnected

snack_dict = {'tanyi':'garri','mary':'groundnut', 'you':'guess', 'prince':'cakes'}
for i in snack_dict.values():
    print(i)

word = text.split(' ')
for i in word:
    print(i)


import random
print('lets play a guessing game! you have 3 tries to guess a number between 1 and 10')
#get the number from user

for i in range(1,4):
    print('type a number! ')
    while True:
        guess = input()
        if guess.isdecimal():
            break
        print('type a number! ')
        print()
        
    systemnumber = random.randint(1, 20)
    if guess == systemnumber:
        print('you got it')
        break
    else:
        print(3-i,' attempt(s) left')
        print()

