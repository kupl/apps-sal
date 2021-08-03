from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    lis = [arr[0]]
    lis += [arr[i] for i in range(1, n) if(arr[i - 1] != arr[i])]
    if(len(set(lis)) != len(lis)):
        print("NO")
    else:
        c = dict(Counter(arr))
        if(len(set(c.values())) == len(c)):
            print("YES")
        else:
            print("NO")
