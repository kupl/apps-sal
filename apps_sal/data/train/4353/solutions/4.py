def could_be(original, another):
    original_words = original.split()
    another_words = another.split()
    if not original_words or not another_words:
        return False
    return all((w in original_words for w in another_words))
