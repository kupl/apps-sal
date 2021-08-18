for t in range(int(input())):
    path = input()
    mx = 0
    it = 0
    count = 0

    while it < len(path):

        if path[it] == '.':
            temp = 0

            while path[it] == '.':
                temp += 1
                it += 1

            if temp > mx:
                count += 1
                mx = temp

        else:
            it += 1

    print(count)
