# cook your dish here
pricess,have=input().split()
allPrices=[int(i) for i in input().split()]
allPrices.sort()
i=0
sum=0
for j in allPrices:
 i=i+1
 sum=sum+j
 if sum>=int(have):
  print(i-1)
  return

