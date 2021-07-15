k = input('')
answer = 0
for i in range(len(k)):
    if k[i] == 'Q':
        for j in range(i + 1, len(k)):
            if k[j] == 'A':
                for z in range(j + 1, len(k)):
                    if k[z] == 'Q':
                        answer += 1
print(answer)
