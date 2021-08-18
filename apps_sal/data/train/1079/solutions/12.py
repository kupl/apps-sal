try:
    t = int(input())

    while(t != 0):
        t -= 1
        n = input()

        k = 0
        for j in range(0, len(n)):
            if(n[j] == '4'):
                k += 1
        print(k)

except:
    pass
