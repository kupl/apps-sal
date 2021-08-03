# cook your dish here
for h in range(int(input())):
    s = input()
    if len(s) != len(set(s)):
        print('yes')
    else:
        print('no')
