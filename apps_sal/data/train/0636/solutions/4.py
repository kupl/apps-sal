inp = input().split()

inp = [int(q) for q in inp]
a = inp[2::]
t = inp[1]

# if len(a) < 4:
#     print("0")
#     exit)

# if tmp[0] + tmp[1] + tmp[2] + tmp[3] < t or tmp[-1] + tmp[-2] + tmp[-3] + tmp[-4] > t:
#     print("0")
#     return

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


printCombination(a, len(a), 4)
res = 0
for x in q:
    if t == sum(x):
        res += 1

print(res)

