for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    mylis = []
    val = 0
    total = 0
    for i in range(n + 1):
        mylis.append([i, lis[i]])
    mylis = sorted(mylis, key=lambda x: x[1])
    i = 0
    j = n
    "'\n    while len(mylis)>0:\n     if val==0:\n      if mylis[i][1]==k:\n       mylis[i][1]-=k\n       print(i,k,0,0)\n       mylis=mylis[i+1:]\n      elif mylis[i][1]>=k:\n       mylis[i][1] -= k\n       print(i, k, 0, 0)\n      else:\n       val=mylis[i][1]\n       mylis[j][1]-=val\n       print()\n    "
    while total < k * n:
        if mylis[0][1] == k:
            mylis[0][1] -= k
            print(mylis[0][0], k, 0, 0)
            mylis = mylis[1:]
            total += k
        elif mylis[0][1] > k:
            mylis[0][1] -= k
            print(mylis[0][0], k, 0, 0)
            total += k
        else:
            val = mylis[0][1]
            print(mylis[0][0], val, mylis[-1][0], k - val)
            mylis = mylis[1:]
            mylis[-1][1] = mylis[-1][1] - (k - val)
            total += k
