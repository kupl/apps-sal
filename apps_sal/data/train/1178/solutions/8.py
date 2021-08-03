def chef_party():
    t = int(input())
    for _ in range(t):
        N = int(input())
        array = input()
        array = array.split()
        array = list(map(int, array))
        num_of_frnds = 0
        array.sort()
        for i in range(N):
            if array[i] <= i:
                num_of_frnds += 1
            else:
                break

        print(num_of_frnds)
        num_of_frnds = 0


chef_party()
