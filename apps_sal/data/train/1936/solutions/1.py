import math


class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = math.ceil(math.log(label + 1, 2))
        res.append(label)
        if level % 2 == 1:
            label = label // 2
            level -= 1
            label = abs(pow(2, level) - label) + pow(2, level - 1) - 1
            res.append(label)

        while(label >= 1):
            if level % 2 == 1:
                level -= 1
                label = label // 2
                res.append(label)
            else:
                label = label // 2
                level -= 1
                res.append(abs(pow(2, level) - label) + pow(2, level - 1) - 1)
        res.pop()

        return res[::-1]

        # return [pow(2,x) for x in range(math.ceil(math.log(label,2)))]
        # l=[]
        # for i in range(1,math.ceil(math.log(label,2))):
        #     if i%2==1:
        #         l.extend([ temp for temp in range(pow(2,i-1),pow(2,i)) ])
        #     else:
        #         l.extend([temp for temp in range(pow(2,i),pow(2,i-1),-1)])
        # return l
