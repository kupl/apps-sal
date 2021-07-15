x = input()
n = 0
for i in range(len(x)):
    if x[i] == 'Q':
        for j in range(i, len(x)):
            if x[j] == 'A':
                for k in range(j, len(x)):
                    if x[k] == 'Q':
                        n += 1
print(n)
