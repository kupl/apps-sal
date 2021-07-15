class Funnel():

    def __init__(self, levels_count=5):

        self.levels_count = levels_count

        self.__levels = [[[] for _ in range(i)] for i in range(1, self.levels_count+1)]

        self.__curr = [0,0]

    def __fill_one(self, d):

        curr = self.__get_curr()
        levels = self.__levels
        N = self.levels_count

        if not curr:
            return

        levels[curr[0]][curr[1]] = [d]

    def __get_curr(self):

        curr = None

        for k, level in enumerate(self.__levels):
            if [] in level:
                curr = [k, level.index([])]
                break

        return curr

    def fill(self, *args):
        for d in args:
            self.__fill_one(d)

    def drip(self):

        if not self.__levels[0][0]:
            return None

        r = self.__levels[0][0][0]

        self.__levels[0][0] = []

        N = self.levels_count

        hole = [0, 0]

        while hole:

            if hole[0] + 1 >= N:
                break

            a = [hole[0] + 1, hole[1]]
            b = [hole[0] + 1, hole[1] + 1]

            if self.__levels[a[0]][a[1]] == [] and self.__levels[b[0]][b[1]] == []:
                break

            c = max(a, b, key=lambda x: len(self.__get_childs(x[0], x[1])))

            self.__levels[hole[0]][hole[1]] = self.__levels[c[0]][c[1]]

            hole = c

            self.__levels[hole[0]][hole[1]] = []

            self.__curr = hole

        return r


    def __get_childs(self, level_i, list_j):

        N = self.levels_count

        delta = N - level_i

        r = [self.__levels[level_i][list_j]] + [self.__levels[level_i+k][list_j:list_j+k+1] for k in range(1, delta)]

        r = [v2 for v1 in r for v2 in v1 if v2 != []]
        
        return r

    def __str__(self):

        N = self.levels_count

        pr = []

        for l in self.__levels:
            t = " ".join([str(e[0]) if len(e)==1 else " " for e in l])
            n = (2 * N - 1 - len(t))//2
            t = " " * n + "\\" + t + "/"
            pr.append(t)

        return "\n".join(pr[::-1])
