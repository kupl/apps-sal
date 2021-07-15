def queue(queuers,pos):
    count = 0
    while len(queuers) != 0:    #배열이 빌 때까지 반복
        k = queuers.pop(0)    #first-in을 pop
        count += 1    #걸리는 시간을 체크
        if k-1 != 0:    #하나 줄여도 0이 아니라면
            queuers.append(k-1)    #다시 배열의 끝에 첨가
            if pos == 0:    #이 때, 우리가 체크하는 index가 0이었다면
                pos = len(queuers) - 1    #배열의 끝 index로 수정
            else:
                pos -= 1
        elif k-1 == 0 and pos == 0:    #우리의 원소가 0되면 반복문 나감
            break
        else:
            pos -= 1    #다른 원소가 0되면 그냥 배열에서 삭제
    return count
