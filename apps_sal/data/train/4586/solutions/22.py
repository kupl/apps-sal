def tv_remote(word):
    
    a = ['abcde123','fghij456','klmno789','pqrst.@0','uvwxyz_/']
    
    start, start_line, count = 0,0,0
    
    for i in word:
        for line in a:
            if i in line:
                count += abs(line.index(i)-start) + abs(a.index(line)-start_line)
                start, start_line = line.index(i), a.index(line)
                
    return count+len(word)
