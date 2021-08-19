from collections import Counter, defaultdict


class Solution:

    def displayTable(self, orders):
        foods = set()
        table_to_food = defaultdict(Counter)
        for (customer, table, food) in orders:
            table_to_food[table][food] += 1
            foods.add(food)
        foods = sorted(foods)
        m = len(table_to_food)
        n = len(foods)
        res = [[None for j in range(n + 1)] for i in range(m + 1)]
        res[0] = ['Table'] + foods
        for (i, table) in enumerate(sorted(table_to_food.keys(), key=int)):
            res[i + 1][0] = str(table)
            for j in range(0, n):
                food = foods[j]
                res[i + 1][j + 1] = str(table_to_food[table][food])
        return res
