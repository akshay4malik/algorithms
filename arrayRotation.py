#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:37:40 2020

@author: akshay
"""

a = [1,2,3,4,5,6,7]

def rotateArray(arr,d,n):
        for i in range(d):
                temp = arr[0]
                for j in range (n-1):
                        arr[j] = arr[j+1]
                arr[n-1] = temp
        return arr

finalres = rotateArray(a,3,7)
print (finalres)

## complexity = O(n*d)
## auxillary space = O(1)


