def valid(hash_t, n, d):
    flag = 0
    for i in range(d):
        for j in range(i + 1, n, d):
            if (hash_t[j] - hash_t[i + 1]) % d != 0:
                flag = 1
                return False

    return True


def num_inversion(hash_t, n, d):
    count = 0
    for i in range(d):
        for j in range(i + 1, n, d):
            for k in range(j, n, d):
                if hash_t[j] > hash_t[k]:
                    count += 1
    return count


tc = int(input())
while tc:
    n, d = input().split()
    n = int(n)
    d = int(d)
    a = [int(x) for x in input().split(" ")]
    if d == 1:
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] > a[j]:
                    count += 1
        print(count)
    else:
        hash_t = [0] * (n + 1)
        for i in range(n):
            hash_t[a[i]] = i + 1

        if not valid(hash_t, n + 1, d):
            print(-1)
        else:
            count = num_inversion(hash_t, n + 1, d)
            print(count)
    tc -= 1
