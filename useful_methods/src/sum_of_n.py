'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''
"""def sum_of_multiples(limit):
    result=0
    for n in range(limit):
        if n!=1:    
            if (n%3==0 or n%5==0):
                result+=n
        else:
            result+=0
    return result 
print sum_of_multiples(1000)     
if sum_of_multiples(1000)==233168:
    print "Success!"
"""

def sum_with_loop(m,d):
    result= 0
    for i in range(m):
        if i!=1 and i%d==0:
            result+=i
    print 'loop result',result 
    return result


def sum_of_n(a,m,d):
    n=((m-a)/d)+1
    print 'number of terms=',n
    total= float((n)*(m+a)/2)
    print 'formula result=',total
    return total

def upper_limit(n,d):
    print 'max limit is',n-(n%d)
    return n-(n%d)
    

print sum_with_loop(10,3)-sum_of_n(3,upper_limit(10,3),3)