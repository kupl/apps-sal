class Solution(object):
    \"\"\"
    使用类似并查集的解法

    # 思路

    有包含关系的为一组，输入每个群组的头索引

    # 注意

    不能直接用并查集，比如 0, 3 连通了, 使用并查集处理到 1, 3 时会将其连通为 0, 1, 3

    \"\"\"

    def peopleIndexes(self, favoriteCompanies):
        \"\"\"
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        \"\"\"

        n_person = len(favoriteCompanies)

        companies = [set(companies) for companies in favoriteCompanies]

        parent = [i for i in range(n_person)]

        for person_a in range(n_person):
            for person_b in range(person_a + 1, n_person):  # 对所有的人两两处理
                if companies[person_a].issubset(companies[person_b]):
                    parent[person_a] = parent[person_b]
                elif companies[person_b].issubset(companies[person_a]):
                    parent[person_b] = parent[person_a]

        roots = set()
        for person in range(n_person):
            root = parent[person]
            while root != parent[root]:
                root = parent[root]
            roots.add(root)
        return sorted(list(roots))



