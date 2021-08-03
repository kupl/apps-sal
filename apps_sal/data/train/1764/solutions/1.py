def solve(emulator):

    def max_height(eggs, drops):
        if eggs == 0 or drops == 0:
            return 0
        return max_height(eggs - 1, drops - 1) + 1 + max_height(eggs, drops - 1)

    low = 1
    high = max_height(emulator.eggs, emulator.drops)
    while low <= high:
        n = min(low + max_height(emulator.eggs - 1, emulator.drops - 1), high)
        if emulator.drop(n):
            high = n - 1
        else:
            low = n + 1
    return low
