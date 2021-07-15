from collections import Counter
for _ in range(int(input())):
    lens = int(input())
    inps = input().strip()
    need = 0
    cinps = Counter(inps)
    hasOne = False
    for i in cinps:
        if cinps[i]%2 == 1:
            if hasOne == False:
                hasOne = True
                continue
            else:
                need += 1
    print(need)





