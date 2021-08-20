def gc_content(seq):
    try:
        result = (seq.count('G') + seq.count('C')) / len(seq) * 100
        result = round(result, 2)
        return result
    except ZeroDivisionError:
        return 0.0
