def jumping_number(number):
    n = str(number)
    value = 0
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) == 1:
            value +=1
    return "Jumping!!" if value == len(n) -1 else "Not!!"
