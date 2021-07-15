def solution(string,markers):
    lst = string.split('\n')
    ans = []
    for line in lst:
        for m in markers:
            if m in line:
                line = line[: line.find(m)].strip()
        ans.append(line) 
    return '\n'.join(ans)
