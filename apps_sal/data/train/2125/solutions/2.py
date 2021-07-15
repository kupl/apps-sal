n,w,h = list(map(int,input().split()))



D = []



original = []



for i in range(n):

  g,p,t = list(map(int,input().split()))



  a = p-t



  p = p if g == 1 else -p



  original.append(())

  D.append((a,p,i))



D.sort()



from bisect import bisect



res = [None]*n



i = 0

while i < len(D):

  a = D[i][0]

  j = bisect(D, (a+1,-n,0), lo=i)

  m = bisect(D, (a,0,0), lo=i,hi=j)



  L = D[i:j]

  R = D[m:j]+D[i:m]



  for t in range(len(L)):

    _,_,d = L[t]

    _,p,_ = R[t]

    if p > 0:

      res[d] = (p,h)

    else:

      res[d] = (w,-p)



  i = j



print('\n'.join(str(x)+' '+str(y) for x,y in res))





# Made By Mostafa_Khaled

