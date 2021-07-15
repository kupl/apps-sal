class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand or len(hand)%W != 0:
            return False
        hand_dict = self.get_hand_dict(hand)
        return self.is_n_straigh_hand(hand_dict, W)
        
    def is_n_straigh_hand(self, hand_dict, W):
        while hand_dict:
            start_hand = min(hand_dict)
            count = hand_dict[start_hand]
            for i in range(start_hand, W + start_hand):
                if i not in hand_dict:
                    return False
                else:
                    hand_dict[i] -= count
                    if hand_dict[i] == 0:
                        del hand_dict[i]
                    elif hand_dict[i] < 0:
                        return False
        return True
    
    def get_hand_dict(self, hand):
        hand_dict = {}
        for h in hand:
            hand_dict[h] = hand_dict.get(h, 0)
            hand_dict[h] += 1
        return hand_dict
    
#         if not hand or len(hand)%W != 0:
#             return False
#         result = [[] * W for _ in range(len(hand)//W)]
#         hand_dict = self.get_dict(hand)
#         return self.is_n_straight_hand(hand_dict, W, result)
    
#     def is_n_straight_hand(self, hand_dict, W, result):
#         while hand_dict:
#             min_hand = min(hand_dict)
#             count = hand_dict[min_hand]
#             for i in range(min_hand, min_hand + W):
#                 if i not in hand_dict:
#                     return False
#                 hand_dict[i] -= count
#                 if hand_dict[i] == 0:
#                     del hand_dict[i]
#                 elif hand_dict[i] < 0:
#                     return False
#         return True
                    
            
    
#     def get_dict(self, hand):
#         hand_dict = {}
#         for i in hand:
#             hand_dict[i] = hand_dict.get(i, 0) + 1
#         return hand_dict

