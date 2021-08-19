(a, b) = map(int, input().split())
n = 10 ** 9 + 7
print(((b - 1) * b * a // 2 + a * (a + 1) * b * b * (b - 1) // 4) % n)
'print((b-1)*b*a//2)\nprint((b-1)*b*a/2)\nprint((b-1)*b*a//2==(b-1)*b*a/2)\nprint(a*(a+1)*b*b*(b-1)//4)\nprint(a*(a+1)*b*b*(b-1)/4)\nprint(a*(a+1)*b*b*(b-1)//4 == a*(a+1)*b*b*(b-1)/4)\n\n# print(((b-1)*a*b//2+(a+1)*a*b*b*(b-1)//4)%1000000007)'
