car = int(input())
while True:
    ope = input()
    car2 = int(input())
    if ope == "+":
        car += car2
        print("= " + str(car))
    elif ope == "-":
        car -= car2
        print("= " + str(car))
    elif ope == "/":
        car /= car2
        print("= " + str(car))
    elif ope == "*":
        car *= car2
        print("= " + str(car))
    elif ope == "break":
        break
    else:
        print("error")
