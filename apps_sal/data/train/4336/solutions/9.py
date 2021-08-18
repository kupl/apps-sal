def mem_alloc(banks):
    banks, redist = tuple(banks), set()
    while banks not in redist:
        redist.add(banks)
        blocks = max(banks)
        index = banks.index(blocks)
        div, mod = divmod(blocks, 16)
        banks = tuple((i != index and bank) + div + ((i - index - 1) % 16 < mod) for i, bank in enumerate(banks))
    return len(redist)
