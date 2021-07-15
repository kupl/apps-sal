def parse_fen(string):
    unicodes = {"p":"\u2659", "n":"\u2658", "b":"\u2657", "r":"\u2656", "q":"\u2655", "k":"\u2654",
                "P":"\u265F", "N":"\u265E", "B":"\u265D", "R":"\u265C", "Q":"\u265B", "K":"\u265A",
                "black":"\u2587", "white":"\uff3f"}
                
    black,white = unicodes["black"],unicodes["white"]     
    empty = [list((black+white))*4 if i % 2 == 0 else list((white+black))*4 for i in range(8)]

    field_one,active,*rest = string.split(" ")   
    rows = field_one.split("/")

    if active != "w":
        rows = [i[::-1] for i in rows[::-1]]
        
    for row_index,row in enumerate(rows):
        count = 0
        for char in row:
            if char.isdigit():
                count += int(char)
            else:
                empty[row_index][count] = unicodes[char]
                count += 1

    return "\n".join(["".join(i) for i in empty])+"\n"
