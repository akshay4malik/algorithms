#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:53:51 2020

@author: akshay
"""
A = [-8, 1, 4, 6, 10, 45,9,7]
ans = 16

def findElements(arr, size, num):
        arrSorted = sorted(arr)
        found = False
        
        i = 0
        r = size-1
        while i < r:
                if arrSorted[i] + arrSorted[r] == num:
                        found = True
                        print (i,r)
                        break
                elif arrSorted[i] + arrSorted[r] < num:
                        i = i + 1
                elif arrSorted[i] + arrSorted[r] > num:
                        r = r - 1
                else:
                        pass
        return found

res = findElements(A,6, 16)
print (res)
        
        

