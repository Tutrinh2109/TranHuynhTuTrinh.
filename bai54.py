# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:18:17 2024

@author: TranHuynhTuTrinh
"""
#Viết phương thức in ra n phần tử của dãy Fibonacy.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
print(fib(10))
