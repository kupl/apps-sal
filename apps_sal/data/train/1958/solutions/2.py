class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizes = {}
        for i, a in enumerate(groupSizes):
            if a in sizes:
                sizes[a].append(i)
            else:
                sizes[a] = [i]
        result = []
        
        for key in sizes.keys():
            if len(sizes[key]) % key == 0:
                result.extend([sizes[key][i*key:(i+1)*key] for i in range(len(sizes[key])//key)])
        # print(sizes)
        return result
