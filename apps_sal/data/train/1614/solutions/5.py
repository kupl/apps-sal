import re


def who_is_winner(pieces_position_list):
    # Your code here!
    tempList = ["".join(["*" for j in range(7)]) + "\t" for i in range(6)]
    for i in pieces_position_list:
        temp = i.split("_")
        columns = ord(temp[0]) - ord("A")
        sign = "1" if temp[1] == "Red" else "2"
        for j in range(len(tempList)):
            if tempList[j][columns] == "*":
                tempList[j] = tempList[j][:columns] + sign + tempList[j][columns + 1:]
                break
        else:
            return "Draw"
        win = GetWin("".join(tempList))
        if win != "Draw":
            print(win)
            return win
    else:
        return "Draw"
    pass


def GetWin(string):
    if re.search(r"1{4,}|1(?:.{7}1){3,}|1(?:.{8}1){3,}|1(?:.{6}1){3,}", string):
        return "Red"
    if re.search(r"2{4,}|2(?:.{7}2){3,}|2(?:.{8}2){3,}|2(?:.{6}2){3,}", string):
        return "Yellow"
    return "Draw"
