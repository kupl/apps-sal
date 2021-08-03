def actual_generator(a, N, start):
    result = []
    if a == 'B':
        result = ['B', 'G'] * (N // 2)
        result.append('B')
    elif a == 'G':
        result = ['G', 'B'] * (N // 2)
        result.append('G')
    else:
        if start == 'B':
            result = ['B', 'G'] * (N // 2)
        elif start == 'G':
            result = ['G', 'B'] * (N // 2)
    return result


for _ in range(int(input())):
    typ = int(input())
    s = input()
    N = len(s)
    array = [s[i] for i in range(N)]
    countG = array.count('G')
    countB = array.count('B')
    if abs(countG - countB) > 1:
        print(-1)
    else:
        defectB = []
        defectG = []
        if countG == countB:
            actual1 = actual_generator('X', N, 'B')
            actual2 = actual_generator('X', N, 'G')
            defect1B = []
            defect1G = []
            defect2B = []
            defect2G = []
            for i in range(N):
                if actual1[i] != array[i] and actual1[i] == 'B':
                    defect1B.append(i)
                elif actual1[i] != array[i] and actual1[i] == 'G':
                    defect1G.append(i)
            for i in range(N):
                if actual2[i] != array[i] and actual2[i] == 'B':
                    defect2B.append(i)
                elif actual2[i] != array[i] and actual2[i] == 'G':
                    defect2G.append(i)
            if len(defect1B) > len(defect2B):
                defectG = defect2G
                defectB = defect2B
            else:
                defectG = defect1G
                defectB = defect1B
        elif countG > countB:
            actual = actual_generator('G', N, 'X')
            defectB = []
            defectG = []
            for i in range(N):
                if actual[i] != array[i] and actual[i] == 'B':
                    defectB.append(i)
                elif actual[i] != array[i] and actual[i] == 'G':
                    defectG.append(i)

        elif countB > countG:
            actual = actual_generator('B', N, 'X')
            defectB = []
            defectG = []
            for i in range(N):
                if actual[i] != array[i] and actual[i] == 'B':
                    defectB.append(i)
                elif actual[i] != array[i] and actual[i] == 'G':
                    defectG.append(i)

        if typ == 0:
            print(len(defectB))
        elif typ == 1:
            print(abs(sum(defectG) - sum(defectB)))
