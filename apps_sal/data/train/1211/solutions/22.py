for i in range(int(input())):
    n = input()
    co = n.count('abc')
    while(co != 0):
        n = n.replace('abc', '')
        co = n.count('abc')
    print(n)
