#!/usr/bin/env python
# coding: utf-8


def find_subarr(input_lst, num):
    for i in range(len(input_lst)):
        summ = 0
        for j in range(i, len(input_lst)):
            summ += input_lst[j]
            if summ == num:
                return i, j
    return ()
    raise NotImplementedError
