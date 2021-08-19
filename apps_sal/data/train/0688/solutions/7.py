# cook your dish here
for i in range(int(input())):
    x = input()
    c = x.count('10') + x.count('01')
    if(x[-1] != x[0]):
        c += 1
    print('uniform' if c <= 2 else 'non-uniform')
