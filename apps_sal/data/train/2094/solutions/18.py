n = int(input())
s = input()
a = s.count('z')
b = (n - a * 4) // 3
print('1 ' * b + '0 ' * a)
