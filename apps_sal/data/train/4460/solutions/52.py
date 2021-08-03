INDEX_TO_WEEKDAY = {
    1: "Sunday", 2: "Monday", 3: "Tuesday",
    4: "Wednesday", 5: "Thursday", 6: "Friday",
    7: "Saturday"}


def whatday(num) -> str:
    try:
        return INDEX_TO_WEEKDAY[num]
    except LookupError:
        return "Wrong, please enter a number between 1 and 7"
