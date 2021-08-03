t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    valid = True
    count = 0
    for j in a:
        if j == 'H':
            count += 1
            if count > 1:
                valid = False
        if j == 'T':
            count -= 1
            if count < 0:
                valid = False
    if valid and count == 0:
        print('Valid')
    else:
        print('Invalid')
