n = input()
arr = list(map(int,n))
n =len(arr)

m = 1
l = 1
s =0
maxIndex = 0
c=0
for i in range(1, n):
    if (arr[i] > arr[i - 1]):
        l = l + 1
    else:
        if (m < l):
            m = l
            maxIndex = i - m
        l = 1
if (m < l):
    m = l
    maxIndex = n - m

for i in range(maxIndex, (m + maxIndex)):
    s+=arr[i]
    c+=1

print(f'{s}:{maxIndex + 1}-{m + maxIndex}')
