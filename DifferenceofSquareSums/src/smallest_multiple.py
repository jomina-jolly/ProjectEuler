'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''
import fractions
def prime_numbers(n):
    p=[]
    for i in range(2,n+1):
        if is_prime(i):
            p.append(i)
        else:
            non_prime.append(i)
    return p   
            
def is_prime(n):
    count=0
    if n==0 or n==1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                count+=1
        if count>0:
            return False
            
        else:
            return True
        
def product(p):
    product=1
    for i in p:
        product*=i
    return product
            
non_prime=[]
prime= prime_numbers(11)
product= product(prime)
for i in range(len(non_prime)-1,0,-1):
    if product%non_prime[i]==0:
        print (product,non_prime[i],product/non_prime[i])
        continue
    else:
        gcd= fractions.gcd(product, non_prime[i])
        product*=(non_prime[i]/gcd)
        print ' gcd for',non_prime[i],(non_prime[i]/gcd)
        
        
print product



