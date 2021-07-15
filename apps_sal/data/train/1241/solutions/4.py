for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ne = 0
    no = 0
    for i in a:
     if i%2 == 0:
      ne += 1
     else:
      no += 1
    if no <= x//2:
     v = 1
    elif ne <= x//2:
     v = (n-x+1)%2
    else:
     v = (x+1)%2
    if v==0:
     print('Walter')
    else:
     print('Jesse')
