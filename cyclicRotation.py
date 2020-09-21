#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:14:31 2020

@author: akshay
"""

a = [1,2,3,4,5,6,7]

def cycleRotate(arr,size):
        temp = arr[size-1]
        
        for i in range (size-1,0,-1):
                arr[i] = arr[i-1]
        
        arr[0] = temp
        return arr

res = cycleRotate(a,7)
print (res)
        

## Order = O(n) have to go through all the elements
## Auxillary space = O(1)
