#!/home/tanyi/study/CCNA/CCNA_online/1_notes/9-week9/python_labs/ccna_class_labs/usr/bin/python3

def multiples(n, limit):
    total=0
    multiples = []
    for i in range(1,limit):
        if i%n==0:
            multiples.append(i)
            total += i
    print('multiples of '+ str(n), multiples)  
    print() 
    print('thier sum is ',total)
    print()

multiples(3, 1000)

def repeat(l):
    c={}
    for i in l:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    
    for k,v in c.items():
        if v>1:
            print(k)
    print()
    
repeat([1,2,3,5,6,4,3,6])


def person():
    person = {}
    name = input('what is your name? ')
    person['name']=name
    print()
    addr = input('where do you live? ')
    person['addr']=addr
    print()
    zipcode = input('what is your zipcode? ')
    person['zipcode']=zipcode
    print()
    age = input('what is your age? ')
    person['age']=age
    print()
    hair_c=input('what is your hair color? ')
    person['hair_color']=hair_c
    print()
    eye_c=input('what is your eye color? ')
    person['eye_color']=eye_c
    print()
    
    for k,v in person.items():
        print(k+':',v)
    
person()