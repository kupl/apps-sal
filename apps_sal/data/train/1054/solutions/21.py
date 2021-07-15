N = int(input())

for i in range(N):
    string = list(input())
    count = 0
    broken = False
    while count <= len(string) // 2:
        if string[count] == "." and string[-count - 1] == ".":
            string[-count - 1] = string[count] = "a"

        elif string[count] == ".":
            string[count] = string[-count - 1]

        elif string[-count - 1] == ".":
            string[-count - 1] = string[count]

        elif string[count] != string[-count - 1]:
            print(-1)
            broken = True
            break

        count += 1

    if not broken:
        print(''.join(string))

