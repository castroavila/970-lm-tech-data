#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : __init__.py
# @created	   : 27-Mar-2023

"""

"""
from funcoes import soma, subtracao, multiplicacao, divisao


def calcule():
    """Execute operation.
    Returns
    -------
    TODO

    """

    a = float(input('Insert number a: '))
    b = float(input('Insert number b: '))
    options_operation = """
        Choose operation:
        1) soma (+)
        2) subtracao (-)
        3) divisao (/)
        4) multiplicacao (*)
        """

    operation = int(input(options_operation))

    if operation == 1:
        output = soma(a, b)
        print(f'soma de {a} + {b} = {output}')

    if operation == 2:
        output = subtracao(a, b)
        print(f'subtracao de {a} - {b} = {output}')
    if operation == 3:
        output = divisao(a, b)
        print(f'divisao de {a} / {b} = {output}')
    if operation == 4:
        output = multiplicacao(a, b)
        print(f'multiplicacao de {a} * {b} = {output}')
