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
        
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left_array = [0]*(n1+1)
    right_array = [0]*(n2+1)
    for i in range(n1):
        left_array[i] = A[p + i - 1]
    for j in range(n2):
        right_array[j] = A[q + j]
    left_array[n1] = float('inf')
    right_array[n2] = float('inf')
    i = 1
    j = 1
    for k in range(p,r):
        if left_array[i] <= right_array[j]:
            A[k] = left_array[i]
            i = i + 1
        else:
            A[k] = right_array[j]
            j = j + 1
            
def merge-sort(A, p, r):
    if p < r:
        q = (p + r) / 2
        merge-sort(A, p, q)
        merge-sort(A, q + 1, r)
        merge(A, p, q, r)
    
