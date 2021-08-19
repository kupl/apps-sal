def repeater(string, n):
    # Habit of escaping double quotes regardless of context
    return '"{}" repeated {} times is: "{}"'.format(string, n, string * n)
