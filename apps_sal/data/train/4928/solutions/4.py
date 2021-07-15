def binRota(arr):
    return [seat for row, seats in enumerate(arr) for seat in seats[::(-1)**row]]

