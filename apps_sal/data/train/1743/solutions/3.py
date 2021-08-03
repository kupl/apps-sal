def collatz_steps(n, steps):
    i = 0
    exp_2, exp_3 = 1, 1
    ind, flag = 0, 0

    for i in range(0, len(steps)):
        if(i == 0 and steps[0] == 'U'):
            exp_3 = exp_3 * 3
            ind = 1
            exp_2 = exp_2 * 2
        else:
            if(steps[i] == 'U'):
                exp_3 = exp_3 * 3
                ind = ind * 3 + exp_2
                exp_2 = exp_2 * 2
            elif(steps[i] == 'D'):
                exp_2 = exp_2 * 2

    i = (exp_3 * n + ind) // exp_2
    while(flag == 0):
        if((exp_2 * i - ind) % exp_3 == 0):
            flag = 1
        else:
            i = i + 1

    return (exp_2 * i - ind) // exp_3
