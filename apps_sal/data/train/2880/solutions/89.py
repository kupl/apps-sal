def seven(m):
    if len(str(m)) == 1:
        if m % 7 == 0:
            return (m, 0)
        else:
            return (m, 0)
    else:
        def last_number(last_number):
            return int(last_number[-1]) * 2

        def helper(res):
            string = ''
            for i in [int(str(res)[i]) for i in range(0, len(str(res)) - 1)]:
                string = string + str(i)
            if len(string) == 1:
                return int(string)
            elif string != '':
                return int(string) - int(last_number(str(res)))
        iterator = 0
        while True:
            if iterator == 0:
                tmp = helper(m)
                iterator += 1
            else:
                if (len(str(tmp)) == 2 or len(str(tmp)) == 1) and tmp % 7 == 0:
                    return (int(tmp), iterator)
                elif (len(str(tmp)) == 2 or len(str(tmp)) == 1) and tmp % 7 != 0:
                    return (int(tmp), iterator)
                else:
                    tmp = helper(tmp)
                    iterator += 1
