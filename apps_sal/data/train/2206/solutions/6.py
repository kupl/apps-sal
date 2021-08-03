n = int(input())
positions = [int(x) for x in input().split(" ")]

output = '1 '

pointer_to_right_wall = n - 1

coins = [False for i in range(len(positions))]
filled = 1

for i in range(len(positions)):
    coins[positions[i] - 1] = True
    if positions[i] - 1 == pointer_to_right_wall:
        count = 0
        while coins[pointer_to_right_wall] == True:
            if pointer_to_right_wall == 0 and coins[0] == True:
                count += 1
                break
            pointer_to_right_wall -= 1
            count += 1
        filled = filled - count + 1
    else:
        filled += 1
    output += str(filled) + ' '

print(output[:-1])
