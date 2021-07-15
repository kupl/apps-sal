# cook your dish here
k = int(input())
act_name = list(map(int, input().split()))
imposter = list(map(int, input().split()))
names = [0 for i in range(1001)]
for num in act_name:
    names[num] += 1
for num in imposter:
    if(names[num] == 0):
        ans = num
    else:
        names[num] -= 1
print(ans)

