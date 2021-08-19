# First we notice that the number of overall operations is equal to the maximum number
# of operations used on a single index.Next we notice that, if we can solve the problem
# in <= X operations, then we can also solve it in <= X + 1 operations.
# This is a monotonic sequence, so we can solve for the minimum value of X with binary search.
# we have to check wether each element can be changed into
# its previous element(count) in the list using a specified number of operations
# if its not possible then we have to check wether current element is greater
# than the previosu element , if it is so, then we have no need to change
# as the list is already in non decreaing form, then we simply replace
# count with the current element
# if it is lesser than count, then there is no way to make the element
# greater than or equal to the previous element using specified number of
# operations and we return to the binary search part to get the next no. of
# operations
def checker(ij):
    count = 0
    for i in range(len(l)):
        # print(count)
        # print(((count-l[i])%m),ij)
        if ((count - l[i]) % m) >= ij:
            if l[i] > count:
                count = l[i]
            else:
                return False
    # print(l)
    return True


n, m = input().split()
n, m = [int(n), int(m)]
l = [int(i) for i in input().split()]
beg = -1
last = m
while beg < last - 1:
    mid = (beg + last) // 2
    counter = checker(mid)
    # print(beg,last)
    if counter:
        last = mid
    else:
        beg = mid
print(beg)
