from collections import Counter
for _ in range(int(input())):
    s = input()
    Length = len(s)
    List = list(s)
    even = 0
    odd = 0
    Dict = Counter(List)
    Len = len(Dict)
    if(Length % 2 != 0):
        for i in Dict:
            if(Dict[i] % 2 == 0):
                even += 1
            else:
                odd += 1
        if(odd == 1):
            print("YES")
        else:
            print("NO")

    else:
        for i in Dict:
            if(Dict[i] % 2 == 0):
                even += 1
            else:
                odd += 1
        if(odd == 0 or odd == 2):
            print("YES")
        else:
            print("NO")
