class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ords = defaultdict(collections.Counter)
        meals = set()
        for (_, T, M) in orders:
            meals.add(M)
            ords[T][M] += 1
        foods = sorted(meals)
        result = [['Table'] + [food for food in foods]]
        for T in sorted(ords, key=int):
            result.append([T] + [str(ords[T][M]) for M in foods])
        return result
