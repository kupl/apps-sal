# Code reuse: https://www.codewars.com/kata/reviews/5ac53889cd661be6ee0013ff/groups/5ac54c24cd661b3753001fba
# if you like this go the link and upvote StefanPochmanns's solution :)
def is_happy(n):
    while n > 4:
        n = sum(int(d)**2 for d in str(n))
    return n == 1


happy_numbers = lambda n: list(filter(is_happy, range(1, n+1)))
