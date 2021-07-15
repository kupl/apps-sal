try:
     t=int(input())
     for i in range(t):
          d=int(input())
          li=list(bin(d))
          print(li.count('1')-1)
except:
     pass

