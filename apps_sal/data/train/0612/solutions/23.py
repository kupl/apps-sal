for _ in range(int(input())):
    s = input()
    flag = False
    if not s.find('101') == -1:
        flag = True
    elif not s.find('010') == -1:
        flag = True
    if flag:
        print('Good')
    else:
        print('Bad')
