class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        desk = collections.defaultdict(collections.Counter)
        meal = set()
        for _, table, food in orders:
            meal.add(food)
            desk[table][food] += 1
        foods = sorted(meal)
        result = [['Table'] + [food for food in foods]]
        for table in sorted(desk, key=int):
            result.append([table] + [str(desk[table][food]) for food in foods])
        return result
