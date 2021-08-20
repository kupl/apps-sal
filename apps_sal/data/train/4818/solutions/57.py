def solution(a, b) -> str:
    if len(a) <= len(b):
        (mini, maxi) = (a, b)
    elif len(a) > len(b):
        (maxi, mini) = (a, b)
    return f'{mini}{maxi}{mini}'
