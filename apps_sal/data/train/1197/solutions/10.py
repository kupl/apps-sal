t = int(input())
for i in range(t):
    n = int(input())
    j = 1
    a = 2
    ans = [1]
    sum1 = set([1, 2])
    while(j < n):
        sum2 = set()
        for k in range(len(ans)):
            sum2.add(ans[k] + a)
        if(len(sum2.intersection(sum1)) == 0):
            ans.append(a)
            sum1 = sum1.union(sum2)
            sum1.add(a * 2)
            j += 1
        else:
            a += 1
    for k in range(len(ans)):
        print(ans[k], end=" ")
    print()
    print(sum(ans))
