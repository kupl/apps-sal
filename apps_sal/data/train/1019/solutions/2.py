# cook your dish here
try:
    for i in range(int(input())):
        n = int(input())
        l = list(map(int, input().strip().split()))
        if(len(l) % 2 == 0):
            print("no")
        else:
            if(l[0] != 1):
                print("no")
            else:
                for i in range(n // 2):
                    if(l[i] != l[n - i - 1]):
                        print("no")
                        break
                    elif(l[i] - l[i + 1] != -1):
                        print("no")
                        break
                else:
                    print("yes")

except:
    pass
