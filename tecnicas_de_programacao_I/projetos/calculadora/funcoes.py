#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : funcoes.py
# @created	   : 27-Mar-2023

"""

"""


def soma(a, b):
    """Add up numbers.

    Parameters
    ----------
    a : TODO
    b : TODO

    Returns
    -------
    TODO

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(
            f'O input `a` e `b` devem ser uma string, recebido {a}, {type(a)}, {b} {type(b)}'
        )

    return a + b


def subtracao(a, b):
    """Substract `b` from `a`.

    Parameters
    ----------
    a : TODO
    b : TODO

    Returns
    -------
    TODO

    """

    return a - b
