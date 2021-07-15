class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = defaultdict(lambda:0)
        for b in B:
            temp = defaultdict(lambda:0)
            for i in b:
                temp[i]+=1
            for k, v in list(temp.items()):
                d[k] = max(v, d[k])
        
        # print(d)
        output = []
        for a in A:
            temp = defaultdict(lambda:0)
            for i in a:
                temp[i]+=1
            # print(temp)
            add = True
            for k , v in list(d.items()):
                if k not in temp or v > temp[k]:
                    add = False
                    break
            if add:
                output.append(a)
        return output

