#!/usr/bin/python3
x = 122
y = 1
for _ in range(26):
    if y == 1:
        print(chr(x), end="")
        x -= 1
        y = 0
    else:
        print(chr(x  - 32),end="")
        x -= 1
        y = 1
