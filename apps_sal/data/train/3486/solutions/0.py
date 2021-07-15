def find_last(n, m):
    li, start = [[0, i + 1] for i in range(n)], 0      # form list of circle with numbers
    while len(li) != 1:
        prev, l_ = li[start][1], len(li)               # starting point and length of circle
        for k in range(m):                             # adding 1 to first m players in circle             
            li[start][0] += 1
            start = (start + 1) % l_

        if m < len(li):                                # if there's anyone left from adding 1 if so..
            k = start
            while li[k][1] != prev:                    # adding 2 to remaining players
                li[k][0] += 2
                k = (k + 1) % l_
                
        li[start][0] += li.pop((start - 1) % l_)[0]    # add last person who receives last 1 coin to next person
        start = [(start - 1) % l_ ,start][start==0]
    return tuple(li[0][::-1])                          # return last person with score and original number
