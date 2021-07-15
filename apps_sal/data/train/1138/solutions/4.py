for t in range(eval(input())):
  n = eval(input())
  v = list(map( int, input().split() ))
  a = []
  ans = 0
  for i in range(n):
    if v[i] == 0 :
      a = [i+1] + a
    else:
      for j in range(len(a)):
        if a[j] == v[i] :
          ans += min( len(a)-j-1, j+1 )
          a = a[:j+1]+[i+1]+a[j+1:]
          break
  print(ans)
