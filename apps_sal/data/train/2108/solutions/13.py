victims = input().split()
print(' '.join(victims))
n = int(input())
for i in range(n):
    (killed, replaced) = input().split()
    if victims[0] == killed:
        victims[0] = replaced
    else:
        victims[1] = replaced
    print(' '.join(victims))
