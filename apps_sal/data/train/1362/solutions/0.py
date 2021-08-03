"""
4
4
4 3 1 2
6
1 2 2 1 3 1
5
10 1 2 10 5
4
1 2 1 2
"""
tests = int(input())

for _ in range(tests):

    n = int(input())
    ls = list(map(int, input().split()))

    if ls[0] < ls[1]:
        ls[0] = -ls[0]

    if ls[-1] < ls[-2]:
        ls[-1] = -ls[-1]

    for i in range(1, n - 1):
        if ls[i] < ls[i - 1] and ls[i] < ls[i + 1]:
            ls[i] = -ls[i]
            '''
      if i > 1 and ls[i - 2] < 0 and ls[i] - ls[i-2] >= ls[i-1]:
       # There can be only one!
       if -ls[i-2] < ls[i]:
        # We win!
        ls[i-2] = -ls[i-2]
        ls[i] = -ls[i]
        #else:
        # They win!
        # Do nothing
      else:
       # We both can go negative
       ls[i] = -ls[i]
      '''

    # print(ls)

    ind = 1

    while ind < n - 1:

        started = False
        pos = []
        while ind < n - 1 and ls[ind] + ls[ind - 1] + ls[ind + 1] <= 0:
            if not started:
                pos.append(ind - 1)
                pos.append(ind + 1)
                started = True
            else:
                pos.append(ind + 1)
            ind += 2

        # print(pos,ls)

        if started:
            rec = [0] * (len(pos) + 1)

            for i in pos:
                ls[i] = -ls[i]

            rec[0] = 0
            rec[1] = ls[pos[0]]

            for i in range(2, len(pos) + 1):
                rec[i] = max(rec[i - 1], ls[pos[i - 1]] + rec[i - 2])

            itr = len(pos)
            while itr > 0:
                if itr == 1 or rec[itr] == ls[pos[itr - 1]] + rec[itr - 2]:
                    ls[pos[itr - 1]] = -ls[pos[itr - 1]]
                    itr -= 2
                else:
                    itr -= 1

        ind += 1

    for i in ls:
        print(i, end=' ')
    print()
