for _ in range(int(input())):

    n = int(input())

    string = list(map(int, input()))

    ds = int(input())

    days = list(map(int, input().split()))

    for d in days:

        index = 0

        itr = 0

        while(itr < d):
            if(string[itr] == '|'):
                index += 1
            index += 1
            itr += 1

        string.insert(index - 1, '|')

        flag = 0

        if(string[0] == 1 and string[1] == 0):
            string[1] = 1
            flag = 1

        for i in range(1, len(string) - 1):

            if(flag == 1):
                flag = 0
                continue

            if(string[i] == 1):

                if(string[i - 1] == 0):
                    string[i - 1] = 1
                if(string[i + 1] == 0):
                    string[i + 1] = 1
                    flag = 1

        if(string[len(string) - 1] == 1 and string[len(string) - 2] == 0):
            string[len(string) - 2] = 1

        # print(string)

    print(string.count(1))
