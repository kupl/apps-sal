class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):

        result = 2 * n
        hashtable = {}
        for seat in reservedSeats:
            if seat[0] not in hashtable:
                hashtable[seat[0]] = {seat[1]}
            else:
                hashtable[seat[0]].add(seat[1])
        for item in hashtable:
            counter = 0
            if 2 not in hashtable[item] and 3 not in hashtable[item] and 4 not in hashtable[item] and 5 not in \\
                    hashtable[item]:
                counter += 1
            if 6 not in hashtable[item] and 7 not in hashtable[item] and 8 not in hashtable[item] and 9 not in \\
                    hashtable[item]:
                counter += 1
            if 4 not in hashtable[item] and 5 not in hashtable[item] and 6 not in hashtable[item] and 7 not in \\
                    hashtable[item] and counter == 0:
                counter += 1
            result += (counter - 2)
        return result

