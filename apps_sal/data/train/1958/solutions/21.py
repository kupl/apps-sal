class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict(enumerate(groupSizes))
        d = {k: v for k, v in sorted(list(d.items()), key=lambda item: item[1])}
        a = []
        b = []

        tmp = next(iter(list(d.values())))
        for k,v in list(d.items()):
            if tmp == v and (len(a) < v):
                a+=[k]
            else:
                b.append(a)
                a = []
                a+= [k]
            if k == (list(d.keys())[-1]):
                b.append(a)
            tmp = v
        return b

