'''
Created on Jul 28, 2016

@author: Vladimir

@description:
Перепаковывает список с именем <list>, который находится в папке <files>
'''

import os
import random
import pickle


def test(lst):
    print('before:\t', lst)
    for idx in range(1, len(lst), 2):
        lst.insert(idx, lst.pop())
    print('after:\t', lst)


if __name__ == '__main__':
    dir_path = 'files'
    lst_path = '%s%s%s' % (dir_path, os.path.sep, 'list')
    if not os.path.exists(lst_path):
        print('File %s is not exists' % lst_path)
        exit(0)
    else:
        file = open(lst_path, mode='rb')
        lst = pickle.load(file)
        test(lst)

    # dir_path = 'files'
    # lst_path = '%s%s%s' % (dir_path, os.path.sep, 'list')
    # print(lst_path)
    # if not os.path.exists(dir_path):
    #     os.mkdir(dir_path)
    # file = open(lst_path, mode='wb')
    # lst = [item for item in range(int(random.random() * 100))]
    # pickle.dump(lst, file)
    # file.close()
