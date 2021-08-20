t = int(input())
lis = []
for i in range(t):
    n = int(input())
    x = int(input())
    expiry = [int(i) for i in input().split()]
    day = 1
    val = x
    expiry.sort()
    while n > 0:
        if expiry[0] > day:
            expiry.pop(0)
            n = n - 1
            val = val - 1
        else:
            lis.append('Impossible')
            break
        if val == 0:
            day += 1
            val = x
    if n == 0:
        lis.append('Possible')
'\n     for i in range(x):\n      if expiry[i]>day:\n       expiry.pop(0)\n       n = n-1\n       if n==0:\n        lis.append("Possible")\n        break\n        #val = False\n      else:\n       lis.append("Impossible")\n       break\n       #val = False\n     day+=1\n'
for i in lis:
    print(i)
