class Solution:
    def alertNames(self, name_list: List[str], time: List[str]) -> List[str]:
        time_list = []
        for ts in time:
            h, m = list(map(int, ts.split(':')))
            time_list.append(h*60 + m)
        res = set()
        A = list(sorted(zip(name_list, time_list)))
        for i, (name, t) in enumerate(A):
            if i + 2 < len(name_list) and name == A[i+2][0] and t >= A[i+2][1] - 60:
                res.add(name)
        return sorted(res)
