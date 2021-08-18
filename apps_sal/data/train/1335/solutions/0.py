n = int(input())
lst = list(map(int, input().split()))
dict1 = {}.fromkeys(lst, 0)
for key in lst:
    dict1[key] += 1
sum1 = 0
for key in dict1:
    sum1 += dict1[key] // 2
    if(dict1[key] % 2 == 1):
        sum1 += 1
print(sum1)
