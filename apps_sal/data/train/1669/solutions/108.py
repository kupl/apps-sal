class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False

        hand = sorted(hand)
        cnt = {}

        for card in hand:
            if card not in cnt:
                cnt[card] = 0
            cnt[card] += 1

        cur_len = 0
        last_val = -1
        num_sub_hands = 0

        unique_vals = sorted(set(hand))
        flag = True

        loops = 0

        while len(cnt) and flag and num_sub_hands < len(hand) // W:
            flag = False
            # pass by value
            tmp = sorted(set(unique_vals))

            for element in tmp:
                loops += 1
                if last_val == -1 or element == last_val + 1:
                    last_val = element
                    cnt[element] -= 1
                    cur_len += 1
                    flag = True
                if cnt[element] == 0:
                    del cnt[element]
                    unique_vals.remove(element)
                if cur_len == W:
                    last_val = -1
                    cur_len = 0
                    num_sub_hands += 1
                    break

        return len(cnt) == 0 and num_sub_hands == len(hand) // W
