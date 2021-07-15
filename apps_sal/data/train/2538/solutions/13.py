class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1, n+1):
            summed = sum([int(k) for k in str(i)])
            if(summed in dic):
                dic[summed].append(i)
            else:
                dic[summed] = [i]
        maximumLen = max([len(value) for value in dic.values()])
        count = 0
        for value in dic.values():
            if(len(value) == maximumLen):
                count += 1
        return count
