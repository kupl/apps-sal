class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
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
            lft_full = A[lft_idx_outer] if lft_idx_outer < len(A) else A[lft_idx_outer - 1]
            rgt_full = B[rgt_idx_outer] if rgt_idx_outer < len(B) else B[rgt_idx_outer - 1]
            return (lft, rgt, lft_full, rgt_full, min(lft_idx_outer, len(A) - 1), min(rgt_idx_outer, len(B) - 1))
        u = (0, 0)
        if u[0] >= len(A) or u[0] >= len(B):
            return []
        (i_a, i_b, next_a2, next_b2, counter_a, counter_b) = get_next_items(u[0], u[1])
        redo_step = True
        while not (i_a is None and i_b is None):
            if i_a is not None and i_b is None:
                (i, u) = (i_a, (u[0] + 1, u[1]))
            elif i_a is None and i_b is not None:
                (i, u) = (i_b, (u[0], u[1] + 1))
            elif i_a < i_b:
                (i, u) = (i_a, (u[0] + 1, u[1]))
            elif i_a > i_b:
                (i, u) = (i_b, (u[0], u[1] + 1))
            elif i_a == i_b and redo_step:
                (i, u) = (i_a, (u[0], u[1]))
                redo_step = False
            elif i_a == i_b and (not redo_step):
                (i, u) = (i_a, (u[0] + 1, u[1] + 1))
                redo_step = True
            if next_a2 is not None and next_b2 is not None and (next_a2[0] <= i <= next_a2[1]) and (next_b2[0] <= i <= next_b2[1]):
                intersections_append2((counter_a, counter_b), i)
            (i_a, i_b, next_a2, next_b2, counter_a, counter_b) = get_next_items(u[0], u[1])
        return self.res2
