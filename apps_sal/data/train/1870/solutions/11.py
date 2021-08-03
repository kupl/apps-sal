class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        output = []
        output.append([i for i, x in enumerate(count) if x][0])
        output.append([i for i, x in enumerate(count) if x][-1])
        nums = sum(count)
        total = 0
        for i, x in enumerate(count):
            if x:
                total += i * x
        output.append(total / nums)
        if nums % 2 == 0:
            curr = 0
            first = ((nums - 2) // 2)
            second = first + 1
            print(first, second)
            firstNum, secondNum = None, None
            for i, x in enumerate(count):
                if x:
                    curr += x
                if not firstNum and curr > first:
                    firstNum = i
                if curr > second:
                    secondNum = i
                if secondNum:
                    output.append((firstNum + secondNum) / 2)
                    break

        else:
            curr = 0

            for i, x in enumerate(count):
                if x:
                    curr += x
                if curr >= (nums - 1) // 2:
                    output.append(i)
                    break
        output.append(count.index(max(count)))
        return output
