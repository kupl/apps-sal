def parity_bit(binary):
    return " ".join(["error" if signal.count("1") & 1 else signal[:-1] for signal in binary.split(" ")])
