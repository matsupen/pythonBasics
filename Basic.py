import math, os, string, os.path, time
import numpy as np
#from matplotlib import pyplot as plt

def quicksort(arr):
    if arr <= 1:
        return arr
    print(arr)

    pivot = [len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def dataType():
    x = 3
    y = 2.5
    print('data type value for X: ', type(x), x)
    print('Multiple Operation on X:', x+1, x-1, x*2, x**2)
    print('Multiple Operation on Y:', type(y), y + 1, x - 1, y * 2, y ** 2)

def dataTypeBool():
    t = 'true'
    f = 'false'
    print('Boolean Operations: ', type(t), t and f, t or f, not t, t!=f)

def string():
    h = 'hello'
    w = 'world'

    print('Length: ', len(h), len(w), 'Word is :', h +' '+w)
    print ('Multiple String Methods: ', h.upper(), h.capitalize(), h.rjust(7), h.center(7), h.replace('o', '(oworld)'), h.strip())

def numpyArray():
    a = np.array ([1, 2, 3])
    print('Array A: ', type(a), a.shape, a[0], a[1], a[2])
    a[0] =5
    print(a[0])
    b = np.array([1 ,2 ,3], [4, 5, 6])
    print('Array B: ', b.shape)




if __name__ == '__main__':

    numpyArray()
    #string()
    #dataTypeBool()
    #print(quicksort([3, 6, 7, 10, 1, 2, 1]))
    #dataType()