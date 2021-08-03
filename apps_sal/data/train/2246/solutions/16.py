import heapq


class Input:
    def __init__(self):
        from sys import stdin
        lines = stdin.readlines()
        self.lines = list([line.rstrip('\n') for line in reversed(lines) if line != '\n'])

    def input(self):
        return self.lines.pop()

    def input_int_list(self):
        return list(map(int, self.input().split()))

    def __bool__(self):
        return bool(self.lines)


def workout_plan(n, k, xs, a, cs):
    choices = []
    cs.reverse()
    total_cost = 0
    for x in xs:
        heapq.heappush(choices, cs.pop())
        while k < x:
            if choices:
                k += a
                total_cost += heapq.heappop(choices)
            else:
                return -1
    return total_cost


inp = Input()
n, k = inp.input_int_list()
xs = inp.input_int_list()
a = int(inp.input())
cs = inp.input_int_list()
print(workout_plan(n, k, xs, a, cs))
