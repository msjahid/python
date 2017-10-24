print("Enter i value: ")
a,b = map(int,input().split())
print("Enter j value: ")
c,d = map(int,input().split())
print("Enter k value: ")
e,f = map(int,input().split())
x = ((c * f) - (e * d))
y = -((a * f) - (b * e))
z = ((a * d) - (b *c))
x1 = str(x) + 'i'
if (y>=0):
    y1 = '+' + str(y) + 'j'
else:
    y1 = str(y) + 'j'
if (z>=0):
    z1 = '+'+ str(z) + 'k'
else:
    z1 = str(z) + 'k'
print(x1 + y1 + z1)
