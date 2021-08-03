def work(n, m, completed):
    chef = []
    asst = []
    total_jobs = list(range(1, n + 1))
    pending = [value for value in total_jobs if value not in completed]
    for k in range(len(pending)):
        if k % 2 == 0:
            chef.append(pending[k])
        else:
            asst.append(pending[k])

    return chef, asst


def main():
    T = int(input())
    for t in range(T):
        jobs = input().split()
        n = int(jobs[0])
        m = int(jobs[1])
        completed = sorted(list(map(int, input().split())))

        chef, asst = work(n, m, completed)
        for j in chef:
            print(j, end=" ")
        print()
        for k in asst:
            print(k, end=" ")
        print()


def __starting_point():
    main()


__starting_point()
