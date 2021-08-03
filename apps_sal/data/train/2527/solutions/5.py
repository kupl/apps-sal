class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF  # from zero to python 32 bits maximum positive integer
        MASK = 0x100000000

        # (a ^ b) is "summing" the bits of a and b
        # For example (where D is decimal and B is binary), 20D == 10100B, and 9D = 1001B
        # Enter the (a & b) << 1 term. This term represents the "carry" for each position. On the next iteration of the while loop, we add in the carry from the previous loop.

        # while b is not 0
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT)

    # All the masks are doing is ensuring that the value is an integer, because your code even has comments stating that a, b, and the return type are of type int. Thus, since the maximum possible int (32 bits) is 2147483647. So, if you add 2 to this value, like you did in your example, the int overflows and you get a negative value. You have to force this in Python, because it doesn't respect this int boundary that other strongly typed languages like Java and C++ have defined.
