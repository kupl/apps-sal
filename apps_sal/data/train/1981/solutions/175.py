from functools import cmp_to_key


def cmp(a, b):
    x1, y1 = a
    x2, y2 = b
    if(x1 < x2):
        return -1
    elif(x1 > x2):
        return -1
    else:
        if(y1 == 'S'):
            return 1
        else:
            return -1


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        N = len(nums)
        M = len(requests)
        l = [0 for i in range(N)]
        l1 = []
        for x, y in requests:
            l1.append((x, 'S'))
            l1.append((y, 'E'))
        l1.sort()
        i = 0
        j = 0
        ct = 0
        while(i < N):
            if(j >= 2 * M):
                l[i] = ct
                i += 1
            elif(i < l1[j][0]):
                l[i] = ct
                i += 1
            elif(i == l1[j][0]):
                ct1 = 0
                while(j < 2 * M and l1[j][0] == i):
                    if(l1[j][1] == 'S'):
                        ct += 1
                    else:
                        ct1 += 1
                    j += 1
                l[i] = ct
                ct -= ct1
                i += 1
            else:
                j += 1

        '''for x,y in requests:
            for i in range(x,y+1):
                l[i] += 1'''

        l.sort(reverse=True)
        nums.sort(reverse=True)
        s = 0
        for i in range(N):
            s += l[i] * nums[i]
        return s % (10**9 + 7)
