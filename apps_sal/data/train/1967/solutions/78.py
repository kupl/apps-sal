class Solution:

    def splitIntoFibonacci(self, S: str):
        max_len = len(S)
        for first_size in range(1, max_len - 1):
            for second_size in range(1, max_len - 1 - first_size):
                res = self.test(S, first_size, second_size)
                if len(res) >= 3 and int(res[-1]) < 2 ** 31 - 1:
                    return res
        return []

    def test(self, s, first_size, second_size):
        cursor = 0
        fibo = []
        first_number = int(s[:first_size])
        if first_size != len(str(first_number)):
            return []
        fibo.append(str(first_number))
        cursor += first_size
        second_number = int(s[cursor:cursor + second_size])
        fibo.append(str(second_number))
        cursor += second_size
        while cursor <= len(s) - 1:
            possible_next = first_number + second_number
            len_next = len(str(possible_next))
            next_number = int(s[cursor:cursor + len_next])
            if cursor + len_next > len(s):
                return []
            elif not next_number == possible_next:
                return []
            fibo.append(str(next_number))
            (first_number, second_number) = (second_number, next_number)
            cursor += len_next
        return fibo
