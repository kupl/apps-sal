class Solution:
    def search(self, locations: List[int], left: int, right: int, target: int):
        while left <= right:
            mid = (left + right) // 2
            if locations[mid] < target:
                left = mid + 1
            elif left == right:
                break
            else:
                right = mid
        return left

    def dfs(self, locations: List[int], start: int, finish: int, fuel: int, memo: List[Dict[int, int]]):
        if fuel in memo[start]:
            return memo[start][fuel]
        if fuel < abs(locations[start] - locations[finish]):
            return 0
        res = 1 if start == finish else 0
        left = self.search(locations, 0, start, locations[start] - fuel)
        right = self.search(locations, start, len(locations) - 1, locations[start] + fuel + 1)
        for next in range(left, right):
            if next == start:
                continue
            res += self.dfs(locations, next, finish, fuel - abs(locations[start] - locations[next]), memo)
        memo[start][fuel] = res % 1000000007
        return memo[start][fuel]

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        startLoc = locations[start]
        finishLoc = locations[finish]
        locations.sort()
        start = self.search(locations, 0, len(locations) - 1, startLoc)
        finish = self.search(locations, 0, len(locations) - 1, finishLoc)
        print((locations, start, finish))
        return self.dfs(locations, start, finish, fuel, [{} for i in range(len(locations))])
