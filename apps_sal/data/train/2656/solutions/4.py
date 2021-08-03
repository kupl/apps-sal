def bird_code(birds):
    codes = []
    for bird in birds:
        words = bird.upper().replace("-", " ").split()
        if len(words) == 1:
            codes.append(words[0][:4])
        elif len(words) == 2:
            codes.append("".join(word[:2] for word in words))
        else:
            code = "".join(word[0] for word in words)
            codes.append(f"{code}{words[2][1] if len(words) == 3 else ''}")
    return codes
