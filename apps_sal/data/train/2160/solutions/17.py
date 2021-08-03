def read():
    return list(map(int, input().split()))


def solve(n, k, A):
    if sum(A) % k != 0:
        print('No')
        return
    target = sum(A) // k
    ans, elems, sm = [], 0, 0
    for num in A:
        sm += num
        elems += 1
        if sm > target:
            print('No')
            return
        if sm == target:
            ans.append(elems)
            elems, sm = 0, 0
    print('Yes')
    print(' '.join(map(str, ans)))


n, k = read()
A = read()
solve(n, k, A)
