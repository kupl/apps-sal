result = []
for i in range(int(input())):
    m = input()
    result.append(''.join(sorted(m, reverse=True)))
for i in range(len(result)):
    print(result[i])
