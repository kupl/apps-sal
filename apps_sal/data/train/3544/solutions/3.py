morse_digits = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]

def morse_converter(stg):
    return int("".join(str(morse_digits.index(stg[i:i+5])) for i in range(0, len(stg), 5)))
