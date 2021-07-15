str1 = list(input())
str2 = list(input())
str1.sort()
str2.sort(reverse=True)
n = len(str1)
str = ['?'] * n
i, j, ni, nj = 0, 0, (n + 1) // 2 - 1, n // 2 - 1
front, rear = 0, n - 1
for cur in range(n):
    if cur & 1 == 0:
        if (str1[i] < str2[j]):
            str[front] = str1[i]
            i += 1
            front += 1
        else:
            str[rear] = str1[ni]
            ni -= 1
            rear -= 1
    else:
        if (str1[i] < str2[j]):
            str[front] = str2[j]
            j += 1
            front += 1
        else:
            str[rear] = str2[nj]
            nj -= 1
            rear -= 1

print(''.join(str))

