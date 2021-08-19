class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        n2s = {i: s for (i, s) in enumerate('abcdefghijklmnopqrstuvwxyz')}
        s2n = {s: i for (i, s) in list(n2s.items())}
        S_res = []
        assert len(S) == len(shifts)
        N = len(S)
        roll_over = 0
        for i in range(N):
            s = S[N - i - 1]
            shift = shifts[N - i - 1]
            roll_over = (shift + roll_over) % 26
            S_res.insert(0, n2s[(s2n[s] + roll_over) % 26])
        return ''.join(S_res)
