#!/home/tanyi/study/CCNA/CCNA_online/1_notes/9-week9/python_labs/ccna_class_labs/usr/bin/python3

for i in range(1,11):
    print(i,end=' ')
print()
print()

l = ["eat","sleep","repeat"]
print(list(enumerate(l)))
print()

def getindex(string, character):
    count = []
    for i in range(len(string)):
        if string[i]==character:
            count.append(i)#to handle multiple occurences
    for i in count:
        print(i,end=' ')#display the values

getindex("input return", 'n')
print()
print()

def shout_words(string):
    text = string.split(' ')
    for i in text:
        print(i.upper()+'!!!')
        
shout_words("Everybody likes bananas") 
print()

def extract_longer(length, sentence):
    found = 0
    count=0
    text = sentence.split(' ')
    for i in text:
        if len(i)>=length:
            print(i)
            found += 1
        else: 
            count = 0  
       
    if count==0 and found == 0:
        print('found no words with characters more than ',length)
        
extract_longer(6, 'sentence and a word length and')
print()

def extract_longer(length, sentence):
    found = []
    text = sentence.split(' ')
    for i in text:
        if len(i)>=length:
            found.append(i) 
            
    if len(found)> 0:
        print(found)
        
    if len(found)== 0:
        print('found no words with characters more than ',length)
        
extract_longer(5, "Try not to interrupt the speaker")

print()

