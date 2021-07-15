def solution(string, end):
    return end == '' or end == string[-len(end):len(string)]
