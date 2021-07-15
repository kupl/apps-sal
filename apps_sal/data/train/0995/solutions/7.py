rooms = int(input())
li = list(map(int, input().split()))
keys = int(input())
maxi = 0
temp = []
j = keys
for i in range(keys+1):
    li1 = li[0:i]
    li2= li[len(li) - j:len(li)]
    newli = li1+li2
    j -=1
    tempMax = sum(newli)
    if maxi < tempMax:
        maxi = tempMax
print(maxi)
            
    
    

