# cook your dish here
input()
arr = list(map(int, input().split(' ')))
subarrays = []

temp_arr = []
for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
        temp_arr.append(arr[j])
        subarrays.append(temp_arr.copy())
    temp_arr = []
subarrays.append([arr[-1]])

for query in range(int(input())):
    num = int(input())
    total = 0
    for subarr in subarrays:
        if min(subarr) == num:
            total += 1
    
    print(total)
    
