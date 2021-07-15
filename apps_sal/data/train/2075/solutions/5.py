n, m, k = [int(x) for x in input().split()]
alice = [int(x) for x in input().split()]
bob = [int(x) for x in input().split()]

alice.sort()
bob.sort()

balance = 0
i = n - 1
j = m - 1

while i >= 0 and j >= 0:
    if alice[i] > bob[j]:
        balance += 1
        i -= 1
    elif alice[i] < bob[j]:
        balance -= 1
        j -= 1
    else:
        i -= 1
        j -= 1
    if balance > 0:
        break

if i + 1 + balance > 0:
    print('YES')
else:
    print('NO')


