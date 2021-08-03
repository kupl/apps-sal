def is_palindrome(word: str) -> bool:
    """Tell if the given word is a palindrome."""
    return word[::-1] == word


def build_left_palindrome(word: str) -> str:
    """Build the shorter palindrome adding letters to the left.

    We search the maximal prefix that is a palindrome. Adding the
    corresponding suffix to the left gives the shorter solution.
    """
    length = len(word)
    while not is_palindrome(word[:length]):
        length -= 1
    return word[length:][::-1] + word


def build_right_palindrome(word: str) -> str:
    """Build the shorter palindrome adding letters to the right."""
    return build_left_palindrome(word[::-1])[::-1]


def build_palindrome(word: str) -> str:
    """Add letters to the right or the left of the given word to get the
    shorter palindrome.
    """
    return sorted([
        build_left_palindrome(word),
        build_right_palindrome(word)
    ], key=len)[0]
