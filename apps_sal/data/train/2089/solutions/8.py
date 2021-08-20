def f(t):
    return t | k if s == '|' else t & k if s == '&' else t ^ k


(a, b) = (1023, 0)
for i in range(int(input())):
    (s, k) = input().split()
    k = int(k)
    (a, b) = (f(a), f(b))
print('2\n|', b ^ a ^ 1023, '\n^', 1023 ^ a)
