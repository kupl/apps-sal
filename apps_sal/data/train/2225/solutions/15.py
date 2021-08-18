import sys
readline = sys.stdin.readline
read = sys.stdin.read

_, L = list(map(int, readline().split()))
s = read().split()


def grundy(x):
    if x == 0:
        return 0
    r = 1
    while x % 2 == 0:
        x //= 2
        r *= 2
    return r


g = 0
st = [(s, 0)]
while st:
    a, idx = st.pop()
    a0 = []
    a1 = []
    for i in a:
        if len(i) <= idx:
            continue
        if i[idx] == "0":
            a0.append(i)
        else:
            a1.append(i)

    if (a0 and not a1) or (a1 and not a0):
        g ^= grundy(L - idx)

    if a0:
        st.append((a0, idx + 1))
    if a1:
        st.append((a1, idx + 1))

if g:
    print("Alice")
else:
    print("Bob")
