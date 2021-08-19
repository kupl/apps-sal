class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:

        def add(name, n):
            if n is None:
                n = m[name]
            used[name].add(n)
            while m[name] in used[name]:
                m[name] += 1
            return n
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
                    add(name, n)
                    ans.append(f'{name}({n})')
            n = add(raw, None)
            if not added:
                ans.append(f'{raw}({n})' if n else raw)
            if n:
                add(f'{raw}({n})', None)
        return ans
