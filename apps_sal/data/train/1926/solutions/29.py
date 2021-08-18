class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        n1 = num + 1
        n2 = num + 2
        h1 = int(n1**0.5)
        h2 = int(n2**0.5)
        stack = []

        def run(n1, h1):
            for i in range(h1, 0, -1):
                if n1 % i == 0:
                    tmp = n1 // i
                    stack.append((abs(i - tmp), i, tmp))
        run(n1, h1)
        run(n2, h2)
        stack.sort(key=lambda x: x[0])
        return [stack[0][1], stack[0][2]]
