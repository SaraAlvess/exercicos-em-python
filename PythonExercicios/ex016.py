"""
from math import trunc
n = float(input('Digite um número: '))
print('O número digitado foi {}, mas sua porção inteira é {}'.format(n, trunc(n)))
"""
n = float(input('Digite um número: '))
print('O número digitado foi {}, mas sua porção inteira é {}'.format(n, int(n)))
