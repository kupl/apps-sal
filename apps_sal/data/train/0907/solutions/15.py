for i in range(int(input())):
    x = int(input())
    y = input()
    z = y.replace('.', '')
    z = z.replace('HT', '')
    print('Invalid' if len(z) > 0 else 'Valid')
