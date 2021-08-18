

s = input()
l = len(s)

instances = [[] for x in range(26)]

s_i = [ord(c) - 97 for c in s]


for i in range(l):
    instances[s_i[i]].append(i)


sum_probability = 0

for c in range(0, 26):
    if not instances[c]:
        continue
    if len(instances[c]) == 0:
        sum_probability += 1
        continue
    max_probability = 0
    for guess in range(1, l):
        num_seen = [0] * 26
        probability = 0
        for index in instances[c]:
            num_seen[s_i[(index + guess) % l]] += 1
        for x in num_seen:
            if x == 1:
                probability += 1
        max_probability = max(max_probability, probability)
    sum_probability += max_probability


print(sum_probability / l)
