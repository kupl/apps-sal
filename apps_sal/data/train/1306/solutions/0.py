# cook your dish here
from collections import Counter
for i in range(int(input())):
    s = input().upper()
    res = Counter(s)
    if res["L"] >= 2 and res["T"] >= 2 and res["I"] >= 2 and res["M"] >= 2:
        if len(s) == 9:
            if res["E"] >= 1:
                print("YES")
            else:
                print("NO")
        elif len(s) > 9:
            if res["E"] >= 2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
