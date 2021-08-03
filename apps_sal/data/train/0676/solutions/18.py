# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        names = list(input().split())
        f = set(names)
        maxi = 0
        dict = {i: 0 for i in f}
        for i in names:
            dict[i] += 1
            if dict[i] > maxi:
                name = i
                maxi = dict[i]
            elif dict[i] == maxi:
                if i < name:
                    name = i

        #name = min([i for i in names if dict[i] == max(dict.values())])
        print(name)


except Exception:
    pass
