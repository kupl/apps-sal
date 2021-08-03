for _ in range(int(input())):
    r = int(input())
    while(r != 0):
        k = r % 10
        if(k % 2 == 0):
            print("1")
            break
        r = r // 10
    else:
        print("0")
