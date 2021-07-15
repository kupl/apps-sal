n = int(input())
a, b = 1023, 0

for _ in range(n):
    c, d = input().split()
    d = int(d)

    if c == '|':
        a, b = a | d, b | d
    elif c == '&':
        a, b = a & d, b & d
    elif c == '^':
        a, b = a ^ d, b ^ d

print('2\n| {}\n^ {}'.format(a ^ b ^ 1023, a ^ 1023))



# Made By Mostafa_Khaled

