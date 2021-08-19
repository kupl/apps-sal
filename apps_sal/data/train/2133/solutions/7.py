n = int(input())
ans = 0
ans1 = 0
arr_ans = []
arr_slot = []
for i in range(n):
    arr_slot.append(input())
for i in range(7):
    for j in range(n):
        arr_ans.append(arr_slot[j][i])
    ans = arr_ans.count('1')
    if ans > ans1:
        ans1 = ans
        ans = 0
    arr_ans = []
print(ans1)
