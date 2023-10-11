import random
import numpy as np


def Hamming_Matrix(r):
    t = np.array([[int(digit) for digit in format(i, '0' + str(r) + 'b')] for i in range(2 ** r)])
    idx = [i for i, row in enumerate(t) if sum(row) <= 1]
    t = np.delete(t, idx, axis=0)
    t = np.flip(t, 0)
    g = np.hstack((np.eye(len(t), dtype=int), t))
    h = np.vstack((t, np.eye(r, dtype=int)))
    return g, h


def word_gen(size):
    result = [i % 2 for i in range(size)]
    return result


def Hamming_Matrix_ext(r):
    g, h = Hamming_Matrix(r)
    h = np.append(h, [np.zeros(len(h.T), dtype=int)], axis=0)
    h = np.append(h, np.ones((len(h), 1), dtype=int), axis=1)
    g = np.append(g, np.zeros((len(g), 1), dtype=int), axis=1)
    for i in range(len(g)):
        if sum(g[i]) % 2 == 1:
            g[i][len(g.T) - 1] = 1
    return g, h


def Check_Hamming(g, h, s, r, extend=False):
    e = np.eye(len(g.T), dtype=int)
    x = word_gen(2 ** r - r - 1)
    word = x @ g % 2
    if extend:
        end = 5
    else:
        end = 4

    for step in range(1, end):
        print('\nСлово: ', word)
        index = random.sample(range(0, len(e)), step)
        v_e = word
        for i in index:
            v_e = (v_e + e[i]) % 2
        print('Слово с', step, 'кратной ошибкой: ', v_e)
        b = v_e @ h % 2
        print('Синдром: ', b)
        id_err = s.get(tuple(b), [])
        if id_err == []:
            print('Такой ошибки нет в таблице \n')
        else:
            print('Ошибка: ', id_err)
            if len(id_err) != 0:
                v_e = ((v_e + id_err) % 2)
                print('Слово после исправления ошибки: ', v_e)


def simple_hemming():
    for r in range(2, 5):
        print(f"r = {r}")
        G, H = Hamming_Matrix(r)
        errors = np.eye(len(H), dtype=int)
        S = {tuple(err @ H): err.tolist() for err in errors}
        print(f"G =\n{G}\nH =\n{H}\nSyndroms:\n{S}")
        Check_Hamming(G, H, S, r)


def extend_hemming():
    r = 3
    G, H = Hamming_Matrix_ext(r)
    errors = np.eye(len(H), dtype=int)
    S = {tuple(err @ H): err.tolist() for err in errors}
    print(f"G =\n{G}\nH =\n{H}\nSyndroms:\n{S}")
    Check_Hamming(G, H, S, r, True)



simple_hemming()
extend_hemming()
