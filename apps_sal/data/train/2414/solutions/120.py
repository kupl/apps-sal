class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        tup_list = []

        for idx1 in range(len(arr)):
            num1 = arr[idx1]
            arr_dict = {}

            for idx2 in range(idx1 + 1, len(arr)):
                num2 = arr[idx2]
                if abs(num1 - num2) <= c:
                    if a in arr_dict:
                        for pot_num2 in arr_dict[a]:
                            if abs(pot_num2 - num2) <= b:
                                tup = (num1, pot_num2, num2)
                                tup_list.append(tup)

                if abs(num1 - num2) <= a:
                    if a in arr_dict:
                        num2_pots = arr_dict[a]
                        num2_pots.append(num2)
                    else:
                        arr_dict[a] = [num2]

        return len(tup_list)
