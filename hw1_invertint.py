#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    number = list(str(number))[::-1]
    if number[len(number)-1] == '-':
        number.insert(0, number.pop(len(number)-1))
    number = ''.join(number)
    return int(number)
    raise NotImplementedError
