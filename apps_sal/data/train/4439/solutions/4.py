def div(x): return len(set(sum([[i, x // i] for i in range(2, int(x**.5) + 1) if not x % i], [])))


d = {**{1: 1, 2: 2}, **{i: div(i) for i in range(3, 12000)}}
def div_num(a, b): return max([[j, i] for i, j in d.items() if a <= i <= b], key=lambda x: x[0], default=[0, 'Error'])[1]
