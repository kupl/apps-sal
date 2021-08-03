class Solution:
    def solve(self, A, target):
        A.sort()
        self.count = 0
        self.count_sixlets(A, 0, target)
        return self.count

    def count_sixlets(self, A, _sum, target):
        if _sum == target:
            self.count += 1
            return

        for i in range(0, len(A)):
            if _sum + A[i] > target:
                break
            self.count_sixlets(A[i + 1:], _sum + A[i], target)


t = int(input())
obj = Solution()
while t > 0:
    n = int(input())
    _sum = int(input())
    _list = list(map(int, input().split()))
    obj.solve(_list, _sum)
    print(obj.count)
    t -= 1
