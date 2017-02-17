def isprime(x):
    x=abs(int(x))
    if x < 2:
        return "Less 2",False
    elif x == 2:
        return True
    elif x % 2 ==0 or x%3==0 or x%5==0 or x%7==0:
        return False
    else:
        for n in range(3,(x**0.5)+2,2):
            if x%n==0:
                return n,False
        return True    
print("Please input your number:")
number =input()

if isprime(number):
    print(number,"is a prime number")
else:
    print(number,"is a composite number")
    
