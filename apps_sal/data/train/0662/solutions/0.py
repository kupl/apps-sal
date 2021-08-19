# cook your dish here
for t in range(int(input().strip())):
    d = int(input().strip())
    L, R = map(int, input().strip().split(" "))
    if L % 2 == 0:
        L += 1
    sum = (((((R - L + 2) // 2) // d) + 1) // 2) - 1
    sum = (sum * 2 * d * (sum + 1) * d) + (sum + 1) * d * (L + d - 1)
    print(sum % 1000000007)
