sentence = "bob saw a big blue boat"
b = 0
x = sentence.count('b')
for i in range (x):
    a = 0 + b
    b = sentence.find('b',a) # b = sentence.index('b',a)
    print(b)
    b = b + 1


'''
sentence = "how can a clam cram in a clean cream can?"
b = 0
x = sentence.count('c')
for i in range (x):
    if sentence[0] == 'c':
        print(0)
    else:
        a = 1 + b
        b = sentence.find('c',a)
        print(b)

'''

        
    
'''
a = "Banglades is my country"
a.find('x')
output: -1

a.index('x')
output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

" 'index' and 'find' function are same but main difference is smartness"

'''
