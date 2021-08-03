class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        lst = [0] * n
        for i in range(n):
            a, b = keyTime[i].split(':')
            st = float(a + '.' + b)
            lst[i] = [keyName[i], st]
        lst.sort()
        i = 0
        ans = []
        while i < n:
            name = lst[i][0]
            minn = lst[i][1]
            lst2 = []
            while i < n and lst[i][0] == name:
                lst2.append(lst[i][1])
                i += 1
            lst2.sort()
            if len(lst2) >= 3:
                foo = 0
                for k in range(len(lst2) - 2):
                    if float(format(lst2[k + 2] - lst2[k], '.2f')) <= 1.00:
                        foo = 1
                if foo == 1:
                    ans.append(name)
        ans.sort()
        return ans
