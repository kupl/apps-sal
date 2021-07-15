n = int(input())
nl = [int(x) for x in input().split()]
st = []
ans = 0
for x in nl:
    if st and st[-1] > x:
        ans = max(ans, st[-1]^x)
    elif st:
        while st and st[-1] < x:
            ans = max(ans, st.pop()^x)
        if st:
            ans = max(ans, st[-1]^x)
    st.append(x)
print(ans)

