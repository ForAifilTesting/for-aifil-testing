'''
Created on Jul 28, 2016

@author: Vladimir
'''

import sys
import re
import math


class Options:
    def __init__(self):
        pass

    @staticmethod
    def use_opts(opts):
        args = []
        for opt in opts:
            if re.search(Options.not_required, opt):
                print(Options.opts.get(opt))
            else:
                args.append(opt.split('='))
        if len(args) != 0:
            calculation(args)


Options.opts = {
    '--function': ['sin', 'cos', 'tan'],
    '--argument': 0,
    '--version': 'options v.1.0',
    '--help': """
Usage: [--help] [--version] --function=<name> --argument=<argument>
\nDescription of options:
\t--help\t\t\tReturns the description of program usage
\t--version\t\tReturns the version of the program
\t--function\t\tThe choice of mathematical function, takes one of the following values: sin, cos, tan
\t--argument\t\tArgument of selected mathematical function, can be an integer or float number
"""
}
Options.required = re.compile(r'^(--[a-zA-Z]+=[[a-zA-Z0-9.]+)*$')
Options.not_required = re.compile(r'^(--[a-zA-Z]+)*$')
Options.float = re.compile(r'^([0-9]+\.[0-9]+)?$')
Options.error = '\n\'python options.py --help\' lists available options and usage guide.'


def error(msg):
    print('\nError:', msg, Options.error)
    sys.exit(0)


def calculation(args):
    if len(args) != 2:
        error('\nMissing a required option.')
    else:
        if args[0][0] == '--function':
            name, value = args[0][1], args[1][1]
        else:
            name, value = args[1][1], args[0][1]
        if not (name in Options.opts.get('--function')):
            error('\nFunction \'%s\' not found.' % name)
        if re.search(Options.float, value):
            value = float(value)
        elif value.isdigit():
            value = int(value)
        else:
            error('\nInvalid argument \'%s\'. Argument must be integer or float number.' % value)
        result = {
            'sin': lambda x: print('sin(%s) = %s' % (x, math.sin(x))),
            'cos': lambda x: print('cos(%s) = %s' % (x, math.cos(x))),
            'tan': lambda x: print('tan(%s) = %s' % (x, math.tan(x)))
        }[name](value)


def args_validation(argv):
    if len(argv) < 2 or len(argv) > 5:
        error('Invalid number of arguments.')

    for arg in argv[1:]:
        if re.search(Options.not_required, arg):
            if not (arg in Options.opts):
                error('\nUnknown option \'%s\'.' % arg)

        elif re.search(Options.required, arg):
            if not (arg.split('=')[0] in Options.opts):
                error('Unknown option \'%s\'.' % arg)
        else:
            error('n\Invalid option format\'%s\'. %s' % arg)
    return argv[1:]


def test(argv):
    args = args_validation(argv)
    Options.use_opts(args)


if __name__ == '__main__':
    test(sys.argv)
