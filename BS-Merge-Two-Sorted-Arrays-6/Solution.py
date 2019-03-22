'''
Created on Mar 21, 2019

@author: J
'''

class Solution:
    
    @staticmethod
    def mergeSortedArray(A,B):
        
        # A or/and B empty
        if len(A) == 0:
            if len(B) == 0:
                return A
            else:
                return B
            
        if len(B) == 0:
            if len(A) == 0:
                return B
            else:
                return A
            
        i, j = 0, 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        
        if i == len(A):
            if j < len(B):
                C = C + B[j:]   
        elif j == len(B):
            if i < len(A):
                C = C + A[i:] 
            
        return C         



A = [7]
B = [5,7]
print("THe answer is [5,7,7], the calculation result is " + str(Solution.mergeSortedArray(A, B))) 

A=[1,2,3,4]
B=[2,4,5,6]
print("THe answer is [1,2,2,3,4,4,5,6], the calculation result is " + str(Solution.mergeSortedArray(A, B))) 
               