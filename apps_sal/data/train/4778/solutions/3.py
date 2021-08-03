def most_money(s):
    d = {i.name: i.fives * 5 + i.tens * 10 + i.twenties * 20 for i in s}
    return max(d, key=lambda x: d[x]) if len(set(d.values())) != 1 or len(d) == 1 else 'all'
