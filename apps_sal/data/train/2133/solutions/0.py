strings = int(input())
count = [0 for x in range(7)]
for k in range(strings):
    s = input()
    for index in range(7):
        if s[index] == '1':
            count[index] += 1
print(max(count))
