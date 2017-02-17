number = 7
guess = 0
count = 0
print("Guess the number!")
while guess != number:
    guess = int(input("Enter the number :  "))
    count = count + 1
    if guess == number:
        print("You are right!")
    elif guess < number:
        print("It's bigger")
    elif guess > number:
        print("It's not so big.")
    if count > 3:
        print("You are expired. don't try again")
        break
    else:
        print("Good job!")
