#!/home/tanyi/study/CCNA/CCNA_online/1_notes/9-week9/python_labs/ccna_class_labs/usr/bin/python3

mysnack = 'garri'
# #print mysnack 100 times
for i in range(1,101):
    print(i,mysnack)
print()

myfriend_snack= 'groundnut_sweet'
snacks = mysnack+' '+myfriend_snack
#print snacks 100 times
for i in range(1,101):
    print(i,snacks)
print()#just for formating

grocery = ['cakes', 'fruits', 'sweets', 'bobolo', 'groundnut_sweet']
print('grocery before fast swap', grocery)
print()
print('is myfriend_snack in grocery? ',myfriend_snack in grocery)
print()

if myfriend_snack in grocery:
    index = grocery.index(myfriend_snack)
    removed = grocery.pop(index)
    print('the removed item is '+removed)
    grocery.insert(index, mysnack)
    print()
    if mysnack in grocery:
        print('the added item is '+mysnack)

print()
print('grocery after fast swap', grocery)