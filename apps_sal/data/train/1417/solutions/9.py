for j in range(int(input())):
    n = int(input())
    nums = input().strip()
    octave = []
    for i in set(nums):
        octave.append(nums.count(i))
    octave.sort()
    if len(set(nums)) == 9:
        print(octave[0])
    else:
        print(0)
