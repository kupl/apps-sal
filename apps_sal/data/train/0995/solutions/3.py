rooms = int(input())
li = list(map(int, input().split()))
keys = int(input())
maxi = 0
j = keys
for i in range(int(keys / 2) + 1):
    newli1 = li[0:i] + li[len(li) - j:len(li)]
    newli2 = li[0:j] + li[len(li) - i:len(li)]
    j -= 1
    if maxi < sum(newli1):
        maxi = sum(newli1)
    if maxi < sum(newli2):
        maxi = sum(newli2)
print(maxi)
