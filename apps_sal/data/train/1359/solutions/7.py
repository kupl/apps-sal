# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 1000000001
    for i in a:
        if i % 2 != 0:
            odd = i
            break
    even = 1000000002
    for i in a:
        if i % 2 == 0:
            even = i
            break
    even_res = 0
    odd_res = 0
    for i in a:
        if i != even:
            if abs(i - even) % 2 == 0:
                even_res += 2
            else:
                even_res += 1
        if i != odd:
            if abs(i - odd) % 2 == 0:
                odd_res += 2
            else:
                odd_res += 1

    print(min(even_res, odd_res))
