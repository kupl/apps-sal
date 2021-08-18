N = int(input())
psychos = list(map(int, input().split(" ")))
time_of_death = [0 for i in range(N)]

stack = [(psychos[0], 0)]
for index, p in enumerate(psychos):
    if index == 0:
        continue
    if p < stack[-1][0]:
        stack.append((p, 1))
        time_of_death[index] = 1

    elif p > stack[-1][0]:
        max_time = -1
        while stack != [] and p > stack[-1][0]:
            max_time = max(max_time, stack[-1][1])
            del stack[-1]
        if stack == []:
            stack.append((p, 0))
            time_of_death[index] = 0
        else:
            stack.append((p, max_time + 1))
            time_of_death[index] = max_time + 1

print(max(time_of_death))


'''
7
15 9 5 10 7 11 14
'''
