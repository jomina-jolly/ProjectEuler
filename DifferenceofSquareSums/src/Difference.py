'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''
def sumOfSquares(n):
    sum_of_square=(n*(n+1)*(2*n+1))/6
    return sum_of_square
    
def squareOfSum(n):
    sum_of_n= (n*(n+1))/2
    square_of_sum= sum_of_n**2    
    return square_of_sum


print     squareOfSum(10)-sumOfSquares(10)
