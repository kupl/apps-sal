class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):

                    # print(f'{arr[i]}, {arr[j]}, {arr[k]}')

                    f = abs(arr[i] - arr[j]) <= a
                    # print(f'<{abs(arr[i] - arr[j])}, {a}, {f}>')

                    s = abs(arr[j] - arr[k]) <= b
                    # print(f'<{abs(arr[j] - arr[k])}, {b}, {s}>')

                    t = abs(arr[i] - arr[k]) <= c
                    # print(f'<{abs(arr[i] - arr[k])}, {c}, {t}>')

                    if f and s and t:
                        # print(f'{arr[i]}, {arr[i+1]}, {arr[i+2]}')
                        count += 1

                    # print()

        return count
