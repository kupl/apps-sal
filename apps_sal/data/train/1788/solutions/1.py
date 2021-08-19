from itertools import zip_longest
import random


def choose_move(game_state):

    def is_nim_sum_zero(nums):
        """
        Determines the "nim-sum" of the game. 
        First all the numbers are converted to binary, then 
        added following the rule that "if the binary column 
        has an even number of 1s, put a 0; else put a 1."

          1 1 0
        1 1 1 0
        1 1 0 1
        -------
        0 1 0 1

        If it sums to 0, we win!
        """
        to_add = []
        for num in nums:
            to_add.append(list(bin(num)[2:]))
        to_transpose = [b[::-1] for b in to_add]
        cols = [col for col in zip_longest(*to_transpose, fillvalue=0)]
        sum = 0
        for col in cols:
            if col.count('1') % 2 != 0:
                return False
        return True
    non_empty_piles = [i for i in range(len(game_state)) if game_state[i] != 0]
    if is_nim_sum_zero(game_state):
        pile = random.choice(non_empty_piles)
        quant = random.choice(list(range(1, game_state[pile])) + 1)
    else:
        next_ply = list(game_state)
        pile_ind = 0
        pile = non_empty_piles[pile_ind]
        quant = 1
        next_ply[pile] = next_ply[pile] - quant
        while not is_nim_sum_zero(next_ply):
            next_ply = list(game_state)
            if quant < next_ply[pile]:
                quant += 1
            else:
                pile_ind += 1
                pile = non_empty_piles[pile_ind]
                quant = 1
            next_ply[pile] = next_ply[pile] - quant
    return (pile, quant)
