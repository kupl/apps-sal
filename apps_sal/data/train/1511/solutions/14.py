class check:

    def __init__(self, k, s):
        self.sl = s.split('X')
        self.k = k

    def ans(self):
        answer = 0
        for strings in self.sl:
            irons = []
            magnets = []
            sheets = 0
            for i in range(len(strings)):
                if strings[i] == 'I':
                    if not magnets:
                        irons.append(i + sheets)
                    else:
                        index_i = i + sheets
                        for x in magnets:
                            if self.k + 1 - abs(x - index_i) > 0:
                                answer += 1
                                magnets.remove(x)
                                break
                        else:
                            irons.append(index_i)
                elif strings[i] == 'M':
                    if not irons:
                        magnets.append(i + sheets)
                    else:
                        index_m = i + sheets
                        for x in irons:
                            if self.k + 1 - abs(x - index_m) > 0:
                                answer += 1
                                irons.remove(x)
                                break
                        else:
                            magnets.append(index_m)
                elif strings[i] == ':':
                    sheets += 1
        return answer


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = input()
    st = check(k, s)
    print(st.ans())
