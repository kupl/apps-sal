class CodeforcesTask585ASolution:

    def __init__(self):
        self.result = ''
        self.child_count = 0
        self.child = []

    def read_input(self):
        self.child_count = int(input())
        for x in range(self.child_count):
            self.child.append([x + 1] + [int(y) for y in input().split(' ')] + [True])

    def process_task(self):
        cured = 0
        cured_order = []
        corr_cry = []
        for child in self.child:
            if child[4]:
                cured += 1
                cured_order.append(child[0])
                child[4] = False
                x = child[0]
                power = child[1]
                while x < len(self.child) and power:
                    self.child[x][3] -= power
                    if self.child[x][4]:
                        power -= 1
                    if self.child[x][3] < 0 and self.child[x][4]:
                        corr_cry.append(x + 1)
                        self.child[x][4] = False
                    x += 1
                while corr_cry:
                    crying = corr_cry.pop(0)
                    for x in range(crying, len(self.child)):
                        self.child[x][3] -= self.child[crying - 1][2]
                        if self.child[x][3] < 0 and self.child[x][4]:
                            corr_cry.append(x + 1)
                            self.child[x][4] = False
        self.result = '{0}\n{1}'.format(cured, ' '.join([str(x) for x in cured_order]))

    def get_result(self):
        return self.result


def __starting_point():
    Solution = CodeforcesTask585ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())


__starting_point()
