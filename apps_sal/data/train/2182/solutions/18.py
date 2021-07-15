s1 = list(input())
s2 = list(input())
s1.sort()
s2.sort(reverse=True)
n = len(s1)
s = ['?'] * n
i, j, ni, nj = 0, 0, (n + 1) // 2 - 1, n // 2 - 1
front, rear = 0, n - 1
for cur in range(n):
    if cur & 1 == 0:
        if (s1[i] < s2[j]):
            s[front] = s1[i]
            i += 1
            front += 1
        else:
            s[rear] = s1[ni]
            ni -= 1
            rear -= 1
    else:
        if (s1[i] < s2[j]):
            s[front] = s2[j]
            j += 1
            front += 1
        else:
            s[rear] = s2[nj]
            nj -= 1
            rear -= 1

print(''.join(s))
