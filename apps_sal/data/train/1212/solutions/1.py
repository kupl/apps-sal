def hash_it(arr, s):
    for i in range(len(s)):
        arr[ord(s[i]) - 65] += 1
    arr = sorted(arr, reverse=True)
    return arr


def balance(s, arr, l):
    val = len(set(s))
    res = 10000000000
    pp = 0
    for p in range(1, 27):
        ptr = 0
        if l % p == 0:
            var = l // p
            for q in range(p):
                if arr[q] > var:
                    ptr += arr[q] - var
            for q in range(p, 26):
                if arr[q] > 0:
                    ptr += arr[q]
            res = min(ptr, res)
        pp += 1
    if pp == 26:
        pp = 0
    return res


for _ in range(int(input())):
    s = input()
    l = len(s)
    if l <= 2:
        print(0)
        continue
    arr = [0 for i in range(0, 27)]
    arr = hash_it(arr, s)
    print(balance(s, arr, l))
