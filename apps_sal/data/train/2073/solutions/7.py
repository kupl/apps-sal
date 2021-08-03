def xor(a, b):
    return a ^ b


def solve(l):
    ans = xor(l[0], l[1])
    st = [l[0], l[1]]

    for i in range(2, n):
        while len(st) > 0 and st[-1] < l[i]:
            st.pop()
        st.append(l[i])
        if len(st) >= 2:
            ans = max(ans, xor(st[-1], st[-2]))
    return ans


n = int(input())
l = input()
l = [int(i) for i in l.split()]


ans = solve(l)

l.reverse()

ans = max(ans, solve(l))

print(ans)
