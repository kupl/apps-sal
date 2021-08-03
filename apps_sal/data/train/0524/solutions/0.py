arr = list(input())
n = len(arr)
ans = list()
# for i in arr:
# ans.append(ord(i)-96)
li = ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
s = set(arr)
temp = s.intersection(li)
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    li = list(temp)
    #s = set()
    c = 0
    for i in range(x - 1, y):
        if arr[i] in li:
            c += 1
            li.remove(arr[i])
        if len(li) == 0:
            break
    print(c)
