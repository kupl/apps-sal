def least_rotation(S: str) -> int:
    """Booth's algorithm."""
    f = [-1] * len(S)  # Failure function
    k = 0  # Least rotation of string found so far
    for j in range(1, len(S)):
        sj = S[j]
        i = f[j - k - 1]
        while i != -1 and sj != S[k + i + 1]:
            if sj < S[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != S[k + i + 1]:  # if sj != S[k+i+1], then i == -1
            if sj < S[k]:  # k+i+1 = k
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k


for _ in range(int(input())):
    l, s = input().split()
    if int(l) == 1:
        l = len(s)
        s += s
        k = least_rotation(s)
        print(s[k:k+l])
    else:
        print(''.join(sorted(s)))
