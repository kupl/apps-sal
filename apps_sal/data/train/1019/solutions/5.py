def check_strip(num, strip):
    if(num % 2 == 0):
        return False
    elif(strip[0] != 1):
        return False
    elif(sum(strip) != (((num // 2) + 1)**2)):
        return False
    else:
        return True


try:
    for i in range(int(input())):
        num = int(input())
        strip = list(map(int, input().split()))
        if(check_strip(num, strip)):
            print('yes')
        else:
            print('no')
except Exception as e:
    print(e)
