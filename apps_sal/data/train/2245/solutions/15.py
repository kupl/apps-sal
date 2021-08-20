def process_query(queries, m):
    n = len(queries)
    a = [0] * (m + 1)
    for q in queries:
        a[q[0] - 1] += 1
        a[q[1]] -= 1
    for i in range(1, m):
        a[i] += a[i - 1]
    return a[:-1]


def apply_query(times, updates, n):
    a = [0] * (n + 1)
    for i in range(len(updates)):
        a[updates[i][0] - 1] += times[i] * updates[i][2]
        a[updates[i][1]] -= times[i] * updates[i][2]
    for i in range(1, n):
        a[i] += a[i - 1]
    return a[:-1]


def main():
    (n, m, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    updates = [list(map(int, input().split())) for i in range(m)]
    queries = [list(map(int, input().split())) for i in range(k)]
    times_query = process_query(queries, m)
    updated_a = apply_query(times_query, updates, n)
    print(*[a[i] + updated_a[i] for i in range(n)])


def __starting_point():
    main()


__starting_point()
