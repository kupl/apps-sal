n = int(input())
arr = []
count = 0
for i in range(n):
    x = input()
    while "kh" in x:
        x = x.replace("kh", "h")
    while "u" in x:
        x = x.replace("u", "oo")
    if x not in arr:
        count += 1
        arr.append(x)

print(count)
