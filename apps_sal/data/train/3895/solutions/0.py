def shifted_diff(first, second):
    return (second + second).find(first) if len(first) == len(second) else - 1;
