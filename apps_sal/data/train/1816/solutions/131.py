from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def with_in_one_hour(t1, t3):
            h1, s1 = t1.split(':')
            h3, s3 = t3.split(':')
            return (h1 == h3) or ((int(h3) - int(h1) == 1) and (s1 >= s3))

        res = []
        d = defaultdict(list)

        for n, t in zip(keyName, keyTime):
            d[n].append(t)

        for n, t_list in list(d.items()):
            if len(t_list) > 2:
                t_list.sort()

                for i, t in enumerate(t_list[2:]):
                    if with_in_one_hour(t_list[i], t_list[i + 2]):
                        res.append(n)
                        break

        return sorted(res)
