'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''

def sum_of_n(a,m,d):
    n=((m-a)/d)+1
    total= float((n)*(m+a)/2)
    return total

def upper_limit(n,d):
    return n-(n%d)


n=1000   
result = sum_of_n(0,upper_limit(n-1,5),5)+sum_of_n(0,upper_limit(n-1,3),3)-sum_of_n(0,upper_limit(n-1,15),15)
print 'Find the sum of all the multiples of 3 or 5 below 1000 is',result

    
    


    