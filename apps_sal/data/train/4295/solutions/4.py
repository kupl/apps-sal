def addsides(num):
    output = 0
    print(num)
    if num == "":
        return True
    num = int(num)
    while num != 0:
        output += num % 10
        num = num // 10
    return output


def balanced_num(number):
    number = str(number)
    if len(number) % 2 != 0:
        print(number)
        middle = None
        num1 = number[0:len(number) // 2]
        num2 = number[len(number) // 2 + 1:len(number)]
        print(num1, num2)
        if num1 == None or num2 == None:
            return "Balanced"
        if addsides(num1) == addsides(num2):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        num1 = number[0:len(number) // 2 - 1]
        num2 = number[len(number) // 2 + 1:len(number)]
        if num1 == None or num2 == None:
            return "Balanced"
        if addsides(num1) == addsides(num2):
            return "Balanced"
        else:
            return "Not Balanced"
        print(num1, num2)
