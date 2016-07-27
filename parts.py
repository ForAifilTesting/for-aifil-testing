'''
Created on Jul 28, 2016

@author: Vladimir

@description: Скрипт для просмотра изображений
'''

import random
import pprint
import os


def find_dividend(number, divisor):
    for i in range(number, 0, -1):
        if i % divisor == 0:
            return i
    return 0


def test(n, m):
    div = find_dividend(n, m)
    diff = n - div
    p_size = int(div / m)
    result = {'M': m, 'N size': n, 'N difference': diff, 'N dividend': div, 'Part size:': p_size, 'Parts amount': 0,
              'Result': []}
    if p_size < 2:
        print("Vector %s can not be divided into %s equal parts" % (n, m))
    else:
        diff = int(diff / 2)
        if diff < 3:
            parts = [dict(first=i, last=(i + p_size - 1)) for i in range(0, div, p_size)]
            result['Result'] = parts
            result['Parts amount'] = len(parts)
            return result
        else:
            parts = [dict(first=i, last=(i + p_size - 1)) for i in range(diff, (div + diff), p_size)]
            result['Result'] = parts
            result['Parts amount'] = len(parts)
            return result


if __name__ == '__main__':
    dir_path = 'files'
    vec_path = '%s%s%s' % (dir_path, os.path.sep, 'vector_size.txt')
    ps_path = '%s%s%s' % (dir_path, os.path.sep, 'part_size.txt')
    if not (os.path.exists(vec_path) and os.path.exists(ps_path)):
        print('File %s or %s is not exist' % (vec_path, ps_path))
        exit(0)
    else:
        file, file2 = open(vec_path, mode='r'), open(ps_path, mode='r')
        N, M = file.read(), file2.read()
        if N.isdigit() and M.isdigit():
            pprint.pprint(test(int(N), int(M)))
        else:
            print('Error: %s and %s must be integer' % (N, M))


