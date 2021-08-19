# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    dict1 = {}
    flag = False
    S = [int(x) for x in input().split()]
    for i in range(N):
        if S[i] in dict1.keys():
            dict1[S[i]].append(i + 1)
        else:
            dict1[S[i]] = [i + 1]
    for key, val in dict1.items():
        if len(val) == 1:
            continue
        count = 0
        for e in val:
            if e in dict1.keys():
                count += 1
            if count == 2:
                flag = True
                break
        if flag == True:
            break
    if flag == True:
        print("Truly Happy")
    else:
        print("Poor Chef")
