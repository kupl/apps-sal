from operator import itemgetter
inp = list(map(int, input().split()))
(n, t) = (inp[0], inp[1])
array = inp[2:]
somme = []
for i in range(n - 1):
    for j in range(i + 1, n):
        somme.append((array[i] + array[j], {i, j}))
somme.sort(key=itemgetter(0))
i_end = len(somme) - 1
counter = 0
for i in range(len(somme) - 1):
    while i_end > i and somme[i][0] + somme[i_end][0] > t:
        i_end -= 1
    if i_end == i:
        break
    appo = i_end
    while appo > i and somme[i][0] + somme[appo][0] == t:
        if len(somme[i][1] & somme[appo][1]) == 0:
            counter += 1
        appo -= 1
print(counter // 3)
