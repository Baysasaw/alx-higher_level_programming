#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(x - diff)), end='')
