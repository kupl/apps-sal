def make_set(a):
    size[a] = 1
    parent[a] = a
    anses[a] = A[a]


def find_set(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find_set(parent[a])
    return parent[a]


def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if size[b] > size[a]:
            (a, b) = (b, a)
        parent[b] = a
        size[a] += size[b]
        anses[a] += anses[b]
    return anses[a]


size = dict()
parent = dict()
anses = dict()
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
answer = [0]
for j in range(len(B) - 1, 0, -1):
    j = B[j] - 1
    make_set(j)
    per = anses[j]
    if j + 1 in parent:
        per = union_sets(j, j + 1)
    if j - 1 in parent:
        per = union_sets(j, j - 1)
    ans = max(ans, per)
    answer.append(ans)
for j in range(n - 1, -1, -1):
    print(answer[j])
