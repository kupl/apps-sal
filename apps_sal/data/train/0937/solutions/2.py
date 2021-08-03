t = int(input())
for i in range(t):
    n = input()
    if 'EC' in n:
        print('no')
    elif 'SC' in n or 'SE' in n:
        print('no')
    else:
        print('yes')
