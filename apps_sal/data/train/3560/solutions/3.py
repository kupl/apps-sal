msg = ("He's crap!", "He's ok!", "He's flying!", "Gold!!")
def ski_jump(M):
    l = round(1.35*len(M)**2, 2)
    return f"{l:.2f} metres: {msg[(l>10)+(l>25)+(l>50)]}"
