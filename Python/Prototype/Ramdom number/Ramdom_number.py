import random
a = random.randint(1, 10)
while True:
    b = int(input())
    if a == b:
        print("bingo")
        break
    elif a >= b:
        print("more bigger")
    elif str == type(b):
        print("please entar a number")
    else:
        print("more smaller")