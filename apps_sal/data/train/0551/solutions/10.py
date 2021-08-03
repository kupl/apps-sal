t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    c = 0
    if n != len(set(s)):
        print('yes')
    else:
        print('no')
