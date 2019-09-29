#!/usr/bin/env python
# coding: utf-8


def word_inversion(input_lst):
    k = 0
    while True:
        if input_lst[0] == ' ':
            a = input_lst.pop(0)
            break
        a = input_lst.pop(0)
        input_lst.append(a)
        k += 1
    input_lst.insert(-k, a)
    return None
    raise NotImplementedError
