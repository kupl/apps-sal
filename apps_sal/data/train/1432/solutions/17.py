# cook your dish here

t = int(input())

fact = []
for i in range(500):
    fact.append((i * (i + 1)) // 2)
# print(fact)


def search(fact, n, low, high, key):
    mid = (low + high) // 2
    #print(low, high, mid, fact[mid], fact[mid+1], fact)
    if fact[mid] == key:
        return mid
    elif fact[mid] < key and mid == n - 1:
        return mid
    elif fact[mid] < key and fact[mid + 1] > key:
        return mid
    elif fact[mid] < key and fact[mid + 1] == key:
        return mid + 1
    elif fact[mid] < key:
        return search(fact, n, mid + 1, high, key)
    else:
        return search(fact, n, low, mid - 1, key)


for _ in range(t):
    n = int(input())

    M = [[int(a) for a in input().strip().split()] for i in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            count = count + 1 if M[i][j] == 0 else count

    i = search(fact, len(fact), 0, len(fact), count // 2)
    #print(count, i, fact[i], n, n-i-1)
    print(0 if count >= fact[n - 1] * 2 else n - i - 1)
