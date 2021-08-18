

a, b = map(int, input().split())
n = 10**9 + 7
print(((b - 1) * b * a // 2 + a * (a + 1) * b * b * (b - 1) // 4) % n)
"""print((b-1)*b*a//2)
print((b-1)*b*a/2)
print((b-1)*b*a//2==(b-1)*b*a/2)
print(a*(a+1)*b*b*(b-1)//4)
print(a*(a+1)*b*b*(b-1)/4)
print(a*(a+1)*b*b*(b-1)//4 == a*(a+1)*b*b*(b-1)/4)
