t = int(input())
for y in range(t):
    inptstr = input().split()
    n = int(inptstr[0])
    K = int(inptstr[1])
    s = input()
    noblock = s.split('X')
    cnt = []
    cntiron = 0
    for ele in noblock:
        d = {}
        d1 = {}
        iron = []
        magnet = []
        for x in range(len(ele)):
            if ele[x] == 'I':
                iron.append(x)
            elif ele[x] == 'M':
                magnet.append(x)
        for i in iron:
            for j in magnet:
                if i in d or j in d1:
                    continue
                if i < j:
                    Sij = ele[i:j].count(':')
                if j < i:
                    Sij = ele[j:i].count(':')
                Pij = K + 1 - abs(j - i) - Sij
                if Pij > 0:
                    cntiron = cntiron + 1
                    d[i] = j
                    d1[j] = i
                    break
    print(cntiron)
