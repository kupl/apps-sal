def cost(mins):
    return max(0, -(-(mins - 65)//30)) * 10 + 30
