//
//  Untitled.py
//  5501 Code
//
//  Created by Travis Cox on 2024/8/24.
//

'''
Insertion-Sort(A) from CLRS
'''
def insertion-sort(A):
    #Begin from element 2 (1 in 0-based languages)
    for j in range(1,A.length):
        #key is set to current element, j
        key = A[j]
        #i is set to j-1, to begin search of area already sorted to find where key belongs
        i = j-1
        #Begin while loop, limited by i's counter being greather than or equal to 0 and A[i] (in the sorted area) being greater than key, keep progressing down the array
        while i >= 0 and A[i] > key:
            #Move element in i over one to i+1
            A[i+1] = A[i]
            #Decrement i by one
            i = i - 1
        #Locating where to place key, insert at i+1, i being the location where either A[i] is less than key, or i = -1 in which case key is smallest element thus far
        A[i+1] = key
