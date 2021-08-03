def chessboard(st):
    height, width = map(int, st.split())
    if height == 0 or width == 0:
        return ""
    board = [["*."[(x + y) & 1] for x in range(width)] for y in range(height)]
    return "\n".join(map("".join, board))
