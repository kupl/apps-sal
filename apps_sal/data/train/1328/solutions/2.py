t = int(input())
while t :
    t -= 1 
    n = input().strip()
    x = n.count('4')
    y = n.count('7')
    print(len(n)-x-y)
