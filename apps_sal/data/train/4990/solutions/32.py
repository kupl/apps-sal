def solution(string, ending):
    """Standalone solution."""
    ending_length = len(ending)
    if ending_length == 0:
        return True
    return string[-ending_length:] == ending

def solution_endswith(string, ending):
    """Proper solution using `endswith()`."""
    return string.endswith(ending)
