# cook your dish here
for _ in range(int(input())):
    N = int(input())
    inp_arr = tuple(int(i) for i in input().strip().split())
    chefCoins = {
        5: 0,
        10: 0
    }
    printStr = 'YES'
    for i in inp_arr:
        if(i == 5):
            chefCoins[5] += 1
        elif(i == 10):
            chefCoins[10] += 1
            if(chefCoins[5] > 0):
                chefCoins[5] -= 1
            else:
                printStr = 'NO'
                break
        elif(i == 15):
            if(chefCoins[10] > 0):
                chefCoins[10] -= 1
            elif(chefCoins[5] > 1):
                chefCoins[5] -= 2
            else:
                printStr = 'NO'
                break

    print(printStr)
