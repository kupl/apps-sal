def tv_remote(word):
    count = 0
    index = 0
    remote_dict = {'a' : (1,1), 'b': (2,1), 'c' : (3,1), 'd' : (4,1), 'e' : (5,1), '1' : (6,1), '2' : (7,1), '3' : (8,1),
                   'f' : (1,2), 'g': (2,2), 'h' : (3,2), 'i' : (4,2), 'j' : (5,2), '4' : (6,2), '5' : (7,2), '6' : (8,2),
                   'k' : (1,3), 'l': (2,3), 'm' : (3,3), 'n' : (4,3), 'o' : (5,3), '7' : (6,3), '8' : (7,3), '9' : (8,3),
                   'p' : (1,4), 'q': (2,4), 'r' : (3,4), 's' : (4,4), 't' : (5,4), '.' : (6,4), '@' : (7,4), '0' : (8,4),
                   'u' : (1,5), 'v': (2,5), 'w' : (3,5), 'x' : (4,5), 'y' : (5,5), 'z' : (6,5), '_' : (7,5), '/' : (8,5)}
    
    Xdist = abs(remote_dict[word[index]][0] - remote_dict['a'][0])
    Ydist = abs(remote_dict[word[index]][1] - remote_dict['a'][1])
    count += (Xdist + Ydist + 1)
    
    for index in range(len(word) -1):
        Xdist = 0
        Ydist = 0
        Xdist = abs(remote_dict[word[index]][0] - remote_dict[word[index + 1]][0])
        Ydist = abs(remote_dict[word[index]][1] - remote_dict[word[index + 1 ]][1])
        count += (Xdist + Ydist + 1)
    print(count)
    return count

