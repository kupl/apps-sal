class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = collections.defaultdict(collections.Counter)
        meal = set()
        for _, table, dish in orders:
            meal.add(dish)
            d[table][dish] += 1
        meal = sorted(meal)
        result = [['Table'] + [food for food in meal]]

        for table in sorted(d, key=int):
            result.append([table] + [str(d[table][food]) for food in meal])
        return result
