#best way to solve this problem is by thinking how to solve this problem.
# get permutatation of all the number that can be formed with these sets.
# once you get the set, divide all the set with \":\"
# hour hand should be less than 24, and minutes hand be should be less than 60.
# get all the permutation with that no, and store them in list , and run a compare algorithm, or sort algorithm

import itertools
class Solution:
    def largestTimeFromDigits(self, inputlist):
        allthevalues = list(itertools.permutations(inputlist, 4))
        filteredhourvalue = list(filter(lambda x : x[0]*10 + x[1] < 24 ,allthevalues ))
        filteredminvalue = list(filter(lambda x : x[2]*10 + x[3] < 60 ,filteredhourvalue ))
        if len(filteredminvalue) == 0:
            return \"\"
        else:
            actualtime = list(max(filteredminvalue))
            return \"{}{}:{}{}\".format(*actualtime)





