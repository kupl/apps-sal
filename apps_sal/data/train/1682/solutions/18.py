a = input()
initial, final = 1, 1
cinitial = 1
prev = -1
sum = 0
max = 0
for i in range(len(a)):
    if int(a[i]) > prev:
        sum += int(a[i])
    else:
        if sum > max:
            max = sum
            initial = cinitial
            final = i
        sum = int(a[i])
        cinitial = i + 1
    prev = int(a[i])
if sum > max:
    max = sum
    initial = cinitial
    final = len(a)
print(max, ":", initial, "-", final, sep="")
