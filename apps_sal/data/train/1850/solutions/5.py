class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # first construct graph
        links = [[] for _ in range(N)]
        for a,b in edges:
            links[a].append(b)
            links[b].append(a)
        # --
        sums1 = [0] * N  # botton up
        nums1 = [None] * N  # number of descants (including self)
        sums2 = [0] * N  # top down
        # --
        # dfs1: this time we only sum the chidren's info
        self.dfs1(None, 0, links, sums1, nums1)
        # dfs2: this time from parent to children
        self.dfs2(None, 0, links, sums1, nums1, sums2, 0, 0)
        return [a+b for a,b in zip(sums1, sums2)]
        
    def dfs1(self, p: int, x: int, links, sums1, nums1):
        cur_sum, cur_num = 0, 0
        for x2 in links[x]:
            if x2 != p:
                self.dfs1(x, x2, links, sums1, nums1)
                cur_sum += sums1[x2]
                cur_num += nums1[x2]
        sums1[x] = cur_sum + cur_num  # add 1 for all
        nums1[x] = cur_num + 1  # add self
        # --

    def dfs2(self, p: int, x: int, links, sums1, nums1, sums2, up_num: int, up_sum: int):
        cur_chs = [x2 for x2 in links[x] if x2!=p]
        cur_sums1 = [sums1[z] for z in cur_chs]
        cur_nums1 = [nums1[z] for z in cur_chs]
        all_sums1, all_nums1 = sum(cur_sums1), sum(cur_nums1)
        for x2 in cur_chs:
            tmp_up_num = (up_num+1) + (all_nums1 - nums1[x2])
            tmp_up_sum = up_sum + (all_sums1 - sums1[x2]) + tmp_up_num + (tmp_up_num-(up_num+1))
            sums2[x2] = tmp_up_sum
            self.dfs2(x, x2, links, sums1, nums1, sums2, tmp_up_num, tmp_up_sum)
        # --

