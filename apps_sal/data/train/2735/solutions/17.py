def jumping_number(number):
    number = [int(i) for i in str(number)]
    return "Jumping!!" if all(abs(a - b) == 1 for a, b in zip(number, number[1::])) else "Not!!"
