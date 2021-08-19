import numpy as np


def tv_remote(word):
    num_oks = len(word)
    word = 'a' + word
    anum = 97
    m_ay = n_ay = 5
    m_num = n_num = 3
    posdict_ay = {chr(num): np.asarray(np.divmod(num - anum, n_ay)) for num in np.arange(anum, anum + 25)}
    posdict_num = {str(num + 1): np.divmod(num, n_num) + np.array([0, n_ay]) for num in range(0, 9)}
    posdict_rest = {val: np.divmod(idx, n_num) + np.array([m_num, n_ay]) for (idx, val) in enumerate('.@0z_/')}
    posdict = {**posdict_ay, **posdict_num, **posdict_rest}
    distlist = [np.linalg.norm(posdict[pair[0]] - posdict[pair[1]], ord=1) for pair in zip(word[1:], word[:-1])]
    return sum(distlist) + num_oks
