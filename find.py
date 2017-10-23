sentence = "how can a clam cram in a clean cream canc"
b = 0
x = sentence.count('c')
for i in range (x):
    if sentence[0] == 'c':
        print(0)
    else:
        a = 1 + b
        b = sentence.find('c',a)
        print(b)
        
    
