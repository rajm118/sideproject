import random
to_find = random.randrange(100, 999)

def lets_guess():
    sum__finder()
    divider_finder()
    for i in range(1, 10):
        guess = int(input("What do you think the number is :"))
        if guess == to_find:
            print(" You guessed right \n Congratulations ")
        if i % 3 == 0:
            give_hint(i)
    print("BetterLuck Next time ")

def sum__finder():
    temp = to_find
    sum_=0
    for i in range(3):
        sum_ = sum_ + (temp % 10)
        temp = temp / 10
    print("The sum_ of the 3 digit number is ", int(sum_))

def divider_finder():
    for i in range(1, 10):
        if to_find % i == 0:
            print("The 3 digit number is divisible by ", i)

def give_hint(i):
    temp = to_find
    temp2=0
    for j in range(i // 3):
        temp2 = temp2 + (temp % 10)
        temp = temp / 10
    print("The digit's from  ", int(temp2))

lets_guess()
