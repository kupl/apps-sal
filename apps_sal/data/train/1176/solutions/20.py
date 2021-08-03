# cook your dish here
def change_of_state(state, cur_no):
    if cur_no == 1:
        if state == "R":
            state = "B"
        elif state == "B":
            state = "B"
        elif state == "Y":
            state = "B"
        elif state == "P":
            state = "B"
        elif state == "G":
            state = "B"
    else:
        if state == "R":
            state = "R"
        elif state == "B":
            state = "Y"
        elif state == "Y":
            state = "P"
        elif state == "P":
            state = "G"
        elif state == "G":
            state = "R"
    return state


for _ in range(int(input())):
    s = str(input())
    state = "R"
    for i in range(len(s)):
        state = change_of_state(state, int(s[i]))
    if state == "G":
        print("YES")
    else:
        print("NO")
