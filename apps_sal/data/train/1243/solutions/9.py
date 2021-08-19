# cook your dish here
for i in range(int(input())):
    n = int(input())
    n = str(n)
    z = n.find('5')
    z1 = n.find('0')
    if(z == -1 and z1 == -1):
        print('0')
    else:
        print('1')
