t = int(input())
for _ in range(t):
    str = input()
    new_str = set(str)
    char_freq = []
    for i in new_str:
        char_freq.append(str.count(i))
    char_freq.sort(reverse=True)
    charachter = []
    frepuency = []
    for i in range(1, 27):
        if len(str) % i == 0:
            charachter.append(i)
            frepuency.append(len(str) / i)
    operation = []
    for j in range(len(charachter)):
        p_operation = 0
        n_operation = 0
        for i in range(charachter[j]):
            freq = frepuency[j]
            try:
                t_operation = freq - char_freq[i]
                if t_operation > 0:
                    p_operation += t_operation
                else:
                    n_operation += t_operation
            except:
                break
        n_operation = abs(n_operation)
        operation.append(max(p_operation, n_operation))
    print(int(min(operation)))
