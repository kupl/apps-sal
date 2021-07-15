n = int(input())
arr = [0 for i in range(7)]
for i in range(n):
    s = input()
    for j in range(7):
        if s[j] == '1':
            arr[j] += 1
print(max(arr))
