a = [98, 57, 31, 45, 46]
for _ in range(int(input())):
    S = list(input().strip())
    for x in range(len(S)):
        S[x] = chr((ord(S[x]) - ord('A') + a[x]) % 26 + ord('A'))
    print(''.join(S))
