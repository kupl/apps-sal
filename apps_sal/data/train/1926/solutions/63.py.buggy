class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        minimum = float(\"Inf\")
        upper_bound = int((num + 2) ** 0.5) + 1
        a,b = -1,-1
        for i in range(upper_bound+1 , 0,-1):
            if (num+1) % i == 0:
                first = i
                last = (num+1)// first
                if minimum > abs(first-last):
                    a = first
                    b = last
                    minimum = abs(a-b)
            if (num+2) % i == 0:
                first = i
                last = (num+2) // first
                if minimum > abs(first-last):
                    a = first
                    b = last
                    minimum = abs(a-b)
        return [a,b]
