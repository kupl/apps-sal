class Solution:

    def beautifulArray(self, N: int) -> List[int]:

        def find_array(N: int, dic=defaultdict(list)) -> List[int]:
            if dic[N]:
                pass
            elif N == 1:
                dic[1] = [1]
            else:
                even_N = N // 2
                odd_N = N - even_N
                odd_temp = find_array(odd_N)
                even_temp = find_array(even_N)
                odd_temp = [2 * i - 1 for i in odd_temp]
                even_temp = [2 * i for i in even_temp]
                dic[N] = odd_temp + even_temp
            return dic[N]
        return find_array(N)
