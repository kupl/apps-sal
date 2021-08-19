# cook your dish here
n = input() + "0"

max_sum = 0
max_pos = ""
start = 0
sum = int(n[0])
for i in range(1, len(n)):
    if n[i - 1] >= n[i]:
        if max_sum < sum:
            max_sum = sum
            max_pos = "{}-{}".format(start + 1, i)
        start = i
        sum = int(n[i])
    else:
        sum += int(n[i])
print("{}:{}".format(max_sum, max_pos))
