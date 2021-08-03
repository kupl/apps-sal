def resistor_parallel(*resistors):
    return 1 / (sum(1 / resistor for resistor in resistors))
