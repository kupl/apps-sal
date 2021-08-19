s = input()
# list = [1]
# n = len(s)
# index = 0
# for i in range(1,n):
#     if (s[i-1]=="l") :
#         list.insert(index, i+1)
#     else:
#         index += 1
#         list.insert(index, i+1)
# for num in list:
#     print(num)

n = len(s)
ans = [0] * n
left = n - 1
right = 0
if (s[0] == "l"):
    ans[n - 1] = 1
    left -= 1
else:
    ans[0] = 1
    right += 1
for i in range(1, n):
    if (s[i] == "l"):
        ans[left] = i + 1
        left -= 1
    else:
        ans[right] = i + 1
        right += 1
for num in ans:
    print(num)
