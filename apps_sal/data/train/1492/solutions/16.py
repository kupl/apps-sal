t = int(input())
for i in range(t):
    n = int(input())
    min_a = 1000
    min_b = 1000
    for j in range(n):
        tmp_a = 0
        tmp_b = 0
        str1 = input()
        for e in str1:
            if e == 'a':
                tmp_a += 1
            elif e == 'b':
                tmp_b += 1
        min_a = min(min_a, tmp_a)
        min_b = min(min_b, tmp_b)
    print(min(min_b, min_a))
