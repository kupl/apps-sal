from functools import reduce
# Since it must be less thatn O(n^2) the solution may not involve mul(Array[:]) for each
# element of Array since mul would be O(n-1) and you would do O(n) calls to mul.

# Since it must be less thatn O(n^2) the solution may not involve mul(Array[:]) for each
# element of Array since mul would be O(n-1) and you would do O(n) calls to mul.

# The only way that occurs to me is calling mul just once [that is O(n)] and then mapping / on the
# result Array [that is another O(n)], but since the calls are concatenated the final complexity
# is O(2n)

# Also, since


def product_sans_n(nums):
    # The case for two or more zeros is trivial and can be handled separately:
    # Just a list of N zeroes where N is the length of nums
    if len([x for x in nums if x == 0]) > 1:
        return [0] * len(nums)

    # Now, if there is only one zero this must be stripped from the product P
    # The product can be computed by the functool reduce: this is O(n)
    from operator import mul
    from functools import reduce
    onezero = 0 in nums
    product = reduce(mul, nums if not onezero else nums[:nums.index(0)] + nums[nums.index(0) + 1:])

    # Now, we iterate through the original list dividing the product P by each element
    # The case of one zero is handled separately
    # There is only one list traversing with map: this is O(n)
    if onezero:
        return list(map((lambda x: 0 if x != 0 else product), nums))
    else:
        return list(map((lambda x: product / x), nums))

    # In the end, the algorithm is O(2*n)
