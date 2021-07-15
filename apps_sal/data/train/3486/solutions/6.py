def next_man(people, k):
    while True:
        if people[k] != '.':
            return k
        else:
            if k + 1 >= len(people):
                k = 0
            else:
                k += 1


def find_last(n, m):
    people = [0 for i in range(n)]
    lost_people = n
    k = 0

    while lost_people > 1:

        counter = 0
        while counter < m:
            if people[k] != '.':
                people[k] += 1
                counter += 1
                if k + 1 >= n:
                    k = 0
                else:
                    k += 1
            else:
                if k + 1 >= n:
                    k = 0
                else:
                    k += 1
        if k - 1 < 0:
            sub_money = people[-1]
            people[-1] = '.'
        else:
            sub_money = people[k - 1]
            people[k - 1] = '.'
        k = next_man(people, k)
        people[k] += sub_money
        lost_people -= 1

        whom2 = lost_people - m + 1
        flag = k
        if whom2 > 0:
            for i in range(whom2):
                people[k] += 2
                if k + 1 >= n:
                    k = 0
                else:
                    k += 1
                k = next_man(people, k)
        k = flag

    return k+1, people[k]

