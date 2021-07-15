# First, I coded a straightforward solution. It would work, but because it had to loop over all
# students, and for every student over each locker, it had to do n^2 iterations. With numbers under
# 10k this proved no problem, however the test cases apparently tested bigger numbers, since my
# program kept getting timed out. I decided to record the number of open lockers for each n in range
# 1-500 and discovered a nice pattern: 0 -1-1-1 (3 1's) -2-2-2-2-2 (5 2's) -3-3-3-3-3-3-3 (7 4's)
# - et cetera. In other words, the number of consecutive numbers is (2n + 1). This was still not easy
# to do so I looked up the sequence in OEIS. There, I discovered that the sequence was the integer
# part of the square root of n. Now if that isn't easy to program... more of a maths problem, really.

def num_of_open_lockers(n):
    return int(n**0.5)
