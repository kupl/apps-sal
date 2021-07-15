# code
inp = list(map(int, input().split()))
a = inp[2::]
t = inp[1]

p = []
q = []
def printCombination(arr, n, r):

    data = [0]*r

    combinationUtil(arr, data, 0,
                    n - 1, 0, r)

def combinationUtil(arr, data, start,
                    end, index, r):

    nonlocal q
    nonlocal p
    if (index == r):
        p = []
        for j in range(r):
            p.append(data[j])
        q.append(p)
        return

    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r)
        i += 1


printCombination(a, inp[0], 4)
res = 0
for x in q:
    if t == sum(x):
        res += 1

print(res)

