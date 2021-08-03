def min_sum(arr):
    nums1 = sorted(arr)
    nums2 = sorted(arr, reverse=True)
    return sum([nums1[i] * nums2[i] for i in range(len(nums1) // 2)])
