s1 = input()
s2 = input()

n = len(s1)

s1 = sorted(s1)
s2 = sorted(s2)[::-1]

i = 0
j = 0

res = ["?"]*n
rear = n-1
front = 0

Neven = n % 2 == 0

n1 = (n+1)//2 - 1
n2 = n//2 - 1

for k in range(n):
    if k % 2 == 0:
        if s1[i] < s2[j]:
            res[front] = s1[i]
            front += 1
            i += 1
        else:
            res[rear] = s1[n1]
            rear -= 1
            n1 -= 1
    else:
        if s1[i] < s2[j]:
            res[front] = s2[j]
            front += 1
            j += 1
        else:
            res[rear] = s2[n2]
            rear -= 1
            n2 -= 1

print("".join(res))
