# Without logical operators
def whoseMove(lastPlayer, win):
    return {("black", False): "white",
            ("black", True): "black",
            ("white", False): "black",
            ("white", True): "white", }[(lastPlayer, win)]
