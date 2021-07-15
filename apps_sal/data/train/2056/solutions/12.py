n = int(input())
a = input()
b = input()
count = 0
lst = []
index = 0
while index+1 < n:
    if a[index] != b[index]:
        count += 1
        if a[index] != a[index+1] and a[index] == b[index+1]:
            index += 1
    index += 1
if index < n and a[index] != b[index]:
    count += 1
print(count)

