memory = {1:1, 2:1}
def hofstadter_Q(n):
    if n not in memory.keys():
        memory[n] = hofstadter_Q(n-hofstadter_Q(n-1)) + hofstadter_Q(n-hofstadter_Q(n-2))
    return memory[n]
