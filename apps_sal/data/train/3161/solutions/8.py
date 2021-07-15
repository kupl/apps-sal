def select(memory):
    memory = memory.split(", ")
    hated = []
    for i in range(len(memory)):
        if memory[i].startswith("!"):
            hated.append(memory[i][1:])
            if i != len(memory)-1:
                hated.append(memory[i+1])
    clean_memory = []
    for name in memory:
        if name[0] != "!" and name not in hated:
            clean_memory.append(name)
    return ", ".join(clean_memory)
