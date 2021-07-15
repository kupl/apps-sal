from collections import Counter
noOfSweets = int(input())
typeOfParticularSweet = list(map(int, input().split()))
frequencySweet = Counter(typeOfParticularSweet)
noOfDaysReq = 0
for i in frequencySweet.values():
 if i == 1:
  noOfDaysReq +=1 
 elif i%2 == 0:
  noOfDaysReq += i//2
 else:
  noOfDaysReq += i//2 + 1

print(noOfDaysReq)
