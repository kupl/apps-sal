class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        num = dict()
        for i in range(len(deck)):
            if not deck[i] in list(num.keys()):
                num[deck[i]] = 1
            else:
                num[deck[i]] += 1

        minv = 10005
        for key, value in list(num.items()):
            if value < minv:
                minv = value

        if minv < 2:
            return False

        possible_share = []
        for i in range(2, minv + 1):
            if minv % i == 0:
                possible_share.append(i)

        for i in possible_share:
            Flag = True
            for key, value in list(num.items()):
                if value % i != 0:
                    Flag = False
                    break
            if Flag:
                return True

        return False
