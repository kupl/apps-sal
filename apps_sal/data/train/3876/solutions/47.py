def find(n):
    i = 1
    ans = []
    while i <= n:
        if i % 3 == 0:
            ans.append(i)
        elif i % 5 == 0:
            ans.append(i)
        i += 1
    return sum(ans)

