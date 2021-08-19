import random


class Solution:

    # problem: https://leetcode.com/problems/k-closest-points-to-origin/
    # type : divide and conquer
    # will keep on partitioning and partially sorting part of the values

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def dist(x):
            return points[x][0]**2 + points[x][1]**2

        def partial_sort(i, j, K):
            # i : the start index to sort from, initally will be 0
            # j : the end index, initialy will be len(points) - 1
            # K: # elements to be partially sorted

            if i >= j:
                return

            # 1. pick a random pivot:
            pivot = random.randint(i, j)  # inclusive of j

            # switch with index i, initially will swap with i = 0
            points[i], points[pivot] = points[pivot], points[i]

            # partitions function,
            # will find elements that are smaller than pivot and put to left
            # elements larger than pivot will go to right
            # will return the #sorted elements
            num_sorted = partition(i, j)

            # will have to check if K values are sorted
            # continue after the partition func

            # 1. in case we have sorted more than K elements
            # initially i ==0, but i will change for each iteration
            if K < num_sorted + 1 - i:
                partial_sort(i, num_sorted - 1, K)
            elif K > num_sorted + 1 - i:
                partial_sort(num_sorted + 1, j, K - (num_sorted + 1 - i))

        def partition(i, j):

            # pivot will be at i
            oi = i  # pivot index, old-i
            i += 1  # will keep on checking for the values after oi

            while True:
                # pass 1 -->>
                while i < j and dist(i) < dist(oi):
                    i += 1
                # pass 2 <<-- of j
                while j >= i and dist(j) >= dist(oi):
                    j -= 1
                # stopping condition
                if i >= j:
                    break
                # if it didnt stop, swap i,j
                points[i], points[j] = points[j], points[i]

            # swap pivot with j
            points[oi], points[j] = points[j], points[oi]

            return j

        partial_sort(0, len(points) - 1, K)
        return points[:K]
