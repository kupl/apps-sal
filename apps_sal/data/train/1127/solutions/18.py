t = int(input())
for i in range(t):
    name = input()
    n_names = name.split(' ')
    res = ''
    if (len(n_names) == 3):
        res += n_names[0][0].upper() + ". " + n_names[1][0].upper() + ". " + n_names[2].capitalize()
    elif (len(n_names) == 2):
        res += n_names[0][0].upper() + ". " + n_names[1].capitalize()
    else:
        res += n_names[0].capitalize()
    print(res)
