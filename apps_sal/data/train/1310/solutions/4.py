for _ in range(eval(input())):
 l=list(map(str,input().strip()))
 print(sum([3 if j=='M' else 4 for i,j in enumerate(l) if (i+1)%7!=0]))

