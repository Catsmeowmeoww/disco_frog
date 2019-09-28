#!/usr/bin/env python
# coding: utf-8


def determinant(list_of_list):
    det = 0
    key = 1
    if len(list_of_list) == 1 and len(list_of_list[0]) == 1:
        return list_of_list[0][0]
    for i in range(len(list_of_list)):
        if list_of_list[i][0] == 0:
            continue
        helplst = list(map(list, list_of_list))
        for j in range(len(list_of_list)):
            del helplst[j][0]
        del helplst[i]
        det += list_of_list[i][0]*key * determinant(helplst)
        key = key*(-1)

    return det
    raise NotImplementedError

