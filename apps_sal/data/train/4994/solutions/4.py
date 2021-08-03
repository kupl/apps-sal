def word_problem(
    rules: List[Tuple[str, str]],
    from_str: str,
    to_str: str,
    applications: int
) -> bool:

    def recurse(from_str, applications) -> bool:
        if from_str == to_str:
            yield True
        elif applications == 0:
            yield False
        else:
            for f, t in rules:
                i = from_str.find(f)
                while i > -1:
                    yield from recurse(
                        from_str[:i] + t + from_str[i + len(f):],
                        applications - 1
                    )
                    i = from_str.find(f, i + 1)

    return any(recurse(from_str, applications))
