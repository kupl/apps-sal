def yesOrNo(a, b):
    x = a.count('1')
    y = b.count('1')
    if x % 2 == 1:
        x += 1
    if x < y:
        return 'NO'
    else:
        return 'YES'


a = input()
b = input()
print(yesOrNo(a, b))
