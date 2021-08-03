
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        x = num + 1
        y = num + 2
        a = []
        for i in range(int(x ** 0.5) + 1, -1, -1):
            if x % i == 0:
                a.append([i, x // i])
                break

        for j in range(int(y ** 0.5) + 1, -1, -1):
            if y % j == 0:
                a.append([j, y // j])
                break
        print(a)
        if abs(a[0][0] - a[0][1]) < abs(a[1][0] - a[1][1]):
            return a[0]
        return a[1]
