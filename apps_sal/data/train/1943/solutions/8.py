class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        counter_a = 0
        counter_b = 0
        next_a = A[counter_a] if A else None
        next_b = B[counter_b] if B else None
        max_a = A[-1][1] if A else None
        max_b = B[-1][1] if B else None
        self.k1 = None
        self.k2 = None
        self.res2 = []

        def intersections_append2(k: (int, int), v: int):
            k1 = self.k1
            k2 = self.k2
            if k1 is not None and k2 is not None and (k[0] == k1) and (k[1] == k2):
                if self.res2:
                    self.res2[-1].append(v)
                    if len(self.res2[-1]) > 2:
                        self.res2[-1] = sorted(set(self.res2[-1]))
                else:
                    self.res2.append([v])
            else:
                self.k1 = k[0]
                self.k2 = k[1]
                self.res2.append([v])

        def get_next_items(lft_idx, rgt_idx):
            lft_idx_outer = int(lft_idx / 2)
            lft_idx_inner = lft_idx % 2
            rgt_idx_outer = int(rgt_idx / 2)
            rgt_idx_inner = rgt_idx % 2
            lft = A[lft_idx_outer][lft_idx_inner] if lft_idx_outer < len(A) else None
            rgt = B[rgt_idx_outer][rgt_idx_inner] if rgt_idx_outer < len(B) else None
            return (lft, rgt)
        u = (0, 0)
        (i_a, i_b) = get_next_items(u[0], u[1])
        while i_a is not None and i_b is not None:
            (i_a, i_b) = get_next_items(u[0], u[1])
            if i_a is not None and (i_b is None or i_a <= i_b):
                i = i_a
                u = (u[0] + 1, u[1])
            else:
                i = i_b
                u = (u[0], u[1] + 1)
            while max_a and i <= max_a and (i > next_a[1]):
                counter_a += 1
                next_a = A[counter_a] if counter_a < len(A) else None
            while max_b and i <= max_b and (i > next_b[1]):
                counter_b += 1
                next_b = B[counter_b] if counter_b < len(B) else None
            if next_a and next_b and (next_a[0] <= i <= next_a[1]) and (next_b[0] <= i <= next_b[1]):
                intersections_append2((counter_a, counter_b), i)
        return self.res2
