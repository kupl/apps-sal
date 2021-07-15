for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    
    rem = [0, 0, 0]
    flag = True
    for c in coins:
        change = c - 5
        tens = change//10
        change = change % 10
        fives = change//5
        
        if (rem[0] >= fives and rem[1] >= tens):
            rem[0] -= fives
            rem[1] -= tens
        elif (rem[0] >= (tens*2) + fives):
            rem[0] -= 2
        else:
            flag = False
            break
        rem[c//5-1] += 1 
    
    print("YES" if flag else "NO")
