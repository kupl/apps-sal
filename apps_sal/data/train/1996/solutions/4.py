import collections
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        Terminal = []
        dict_raw = dict()
        dict_idx = collections.defaultdict(list)
        for i, ele in enumerate(graph):
            dict_raw[i] = set(ele)
            if ele==[]: # Terminal
                Terminal.append(i)
            else:
                for idx in ele:
                    dict_idx[idx].append(i) # dict_idx[idx]: what nodes going into node idx
        # Then start from Terminal and do backsearch
        stack = Terminal
        safe = set(Terminal)
        
        while stack:
            node = stack.pop()
            for ele_1 in dict_idx[node]:
                if dict_raw[ele_1].issubset(safe) and ele_1 not in safe: # the 1-step previous node will go to all safe nodes, thus safe
                    safe.add(ele_1)
                    stack.append(ele_1)
        res = list(safe)
        return sorted(res)
                
            

