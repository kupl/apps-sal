class Solution:

    def splitIntoFibonacci(self, s: str) -> List[int]:

        def dfs(start, string, sequence):
            if start == len(string):
                if len(sequence) > 2:
                    return sequence
                return None
            num = 0
            for i in range(start, len(string)):
                if i != start and string[start] == '0':
                    return None
                num = num * 10 + ord(string[i]) - ord('0')
                if num >= 2 ** 31:
                    break
                if len(sequence) > 1 and sequence[-1] + sequence[-2] != num:
                    continue
                sequence.append(num)
                seq = dfs(i + 1, string, sequence)
                if seq != None:
                    return seq
                sequence.pop()
        for sticks in range(2, len(s)):
            seq = dfs(0, s, [])
            if seq:
                return seq
        return []
