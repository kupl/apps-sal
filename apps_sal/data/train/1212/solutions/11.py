t = int(input())
while t:
    s = input()
    n = len(s)
    res = n
    freq = [0] * 26
    for i in s:
        freq[ord(i) - 65] += 1
    freq.sort(reverse=True)
    for i in range(1, 27):
        if(n % i == 0):
            x = 0
            y = n // i
            for j in range(i):
                x += min(y, freq[j])
            res = min(n - x, res)
    print(res)
    t -= 1
