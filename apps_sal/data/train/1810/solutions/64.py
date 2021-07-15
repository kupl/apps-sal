class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        
        used = collections.defaultdict(set)
        m = collections.defaultdict(int)
        
        for raw in names:
            added = False
            res = re.search(f'\\([1-9][0-9]*\\)$', raw)
            if res:
                n = int(res.group(0)[1:-1])
                name = raw[:res.start(0)]
                if n not in used[name]:
                    added = True
                    used[name].add(n)
                    while m[name] in used[name]:
                        m[name] += 1
                    ans.append(f'{name}({n})')
                    
            name = raw
            while m[name] in used[name]:
                m[name] += 1
            n = m[name]
            used[name].add(n)
            if not added:
                ans.append(f'{name}({n})' if n else name)
                
            if n:
                name = f'{name}({n})'
                while m[name] in used[name]:
                    m[name] += 1
                n = m[name]
                used[name].add(n)
        
        return ans
