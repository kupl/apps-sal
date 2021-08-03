class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:

            return False

        freq_dict = collections.Counter(hand)

        while freq_dict:

            min_num = min(freq_dict)

            for i in range(min_num, min_num + W):

                freq = freq_dict[i]

                if freq == 0:

                    return False

                elif freq == 1:

                    del freq_dict[i]

                else:

                    freq_dict[i] -= 1

        return True
