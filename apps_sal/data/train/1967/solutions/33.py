class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:

        def helper(S: str, curr_path: List[int]):
            if not S:
                if self.isValidPath(curr_path):
                    return curr_path
                return None
            for partition_point in range(1, len(S) + 1):
                (prefix, suffix) = (S[:partition_point], S[partition_point:])
                valid_prefix = prefix == '0' or (prefix[0] != '0' and int(prefix) <= 2 ** 31 - 1)
                new_curr_path = curr_path + [int(prefix)]
                if valid_prefix and (len(new_curr_path) < 3 or self.isValidPath(new_curr_path)):
                    recurse = helper(suffix, new_curr_path)
                    if recurse:
                        return recurse
            return None
        return helper(S, [])

    def isValidPath(self, path: List[str]) -> bool:
        return len(path) > 2 and int(path[-1]) == int(path[-2]) + int(path[-3])
