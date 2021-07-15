class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        def within(pt, cen, r2):
            a1, a2 = pt
            p1, p2 = cen
            return (a1 - p1)**2 + (a2 - p2)**2 <= r2

        ans = 1

        for idx, a in enumerate(points):
            for b in points[:idx]:
                a1, a2 = a
                b1, b2 = b

                if (a1-b1)**2+(a2-b2)**2 <= 4*r**2:
                    pos_cir = 0
                    neg_cir = 0

                    mid = ((a1+b1)/2, (a2+b2)/2)
                    perp = (b2-a2, a1-b1)
                    perp_dis = (perp[0]**2 + perp[1]**2)**.5
                    p_dis = (r**2 - ((a1-b1)**2+(a2-b2)**2)/4)**.5

                    cen = (mid[0]+perp[0]*p_dis/perp_dis,
                           mid[1]+perp[1]*p_dis/perp_dis)

                    ocen = (mid[0]+perp[0]*p_dis/perp_dis,
                            mid[1]+perp[1]*p_dis/perp_dis)

                    for c in points:

                        if within(c, cen, r**2+0.00000001):
                            pos_cir += 1
                        if within(c, ocen, r**2+0.00000001):
                            neg_cir += 1

                    ans = max(ans, pos_cir, neg_cir)

        return ans
