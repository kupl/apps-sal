t = int(input())
for T in range(t):
    s = input()
    alpha = [0] * 26
    odd = 0
    for i in s:
        alpha[ord(i) - 97] += 1
    for i in range(26):
        alpha[i] = alpha[i] % 2
        if alpha[i] == 1:
            odd += 1
    if odd <= 2:
        print("YES")
    else:
        print("NO")
