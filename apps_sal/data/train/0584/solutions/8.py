# cook your dish here
try:
    t = int(input())
    while(t):
        n = input()
        x = 0
        f = 0
        if(n[0] == '1'):
            for i in range(1, len(n)):
                if(n[i] == '1' and f == 0):
                    continue
                elif(n[i] == '0'):
                    x += 1
                    f = 1
                    continue
                elif(n[i] == '1' and f == 1):
                    break
        print(x)

        t -= 1
except:
    pass
