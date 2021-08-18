for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = []
    odd = []
    for i in a:
        if(i & 1):
            even.append(i)
        else:
            odd.append(i)
    print(len(even) * len(odd))
