def find_digit(num, nth):
    print(num)
    num=abs(num)
    if nth > len(str(num)):
        return 0
    if nth <= 0:
        return -1
    if nth <= len(str(num)):
        num= str(num)
        return int(num[-nth])
