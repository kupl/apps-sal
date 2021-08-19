def to_mask(word):
    ret = 0
    for c in word:
        ret |= 1 << (ord(c) - 97)
    return ret


def get_good_masks(word):
    BASE = 1 << (ord(word[0]) - 97)
    ret = []

    for choice in range(64):
        mask = BASE
        for i in range(6):
            if (1 << i) & choice:
                mask |= 1 << (ord(word[i + 1]) - 97)
        ret.append(mask)

    return ret


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        # Construct bitmask frequency hashtable
        mask_frequency = defaultdict(int)
        for word in words:
            mask_frequency[to_mask(word)] += 1

        # Calculate
        N = len(puzzles)
        ans = [0] * N
        for i, puzzle in enumerate(puzzles):
            for mask in get_good_masks(puzzle):
                ans[i] += mask_frequency[mask]

        return ans
