'''
Created on Jul 28, 2016

@author: Vladimir
'''

def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result


def test():
    n = input("input N: ")
    sep = ("\n" + "-" * 100)
    if n.isdigit():
        for num in range(1, int(n)):
            tmp = factors(num)
            print(num, "|", tmp, sep)
    else:
        print("The data you entered is not a positive integer")


if __name__ == '__main__':
    test()
