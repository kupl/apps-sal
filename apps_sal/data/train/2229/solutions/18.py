def is_obtained(p, t, K):
    i = 0
    for ch in p:
        i = t.find(ch, i) + 1
        if i == 0:
            return False
        while i in K:
            i = t.find(ch, i) + 1
            if i == 0:
                return False
    return True

I = input

t, p, A = I(), I(), list(map(int, I().split()))
L, R = 0, len(A) - 1

while L < R:
    x = (L + R + 1) // 2
    if is_obtained(p, t, set(A[:x])):
        L = x
    else:
        R = x - 1

print(L)
