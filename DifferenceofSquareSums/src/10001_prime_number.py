'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''

    
#to check a number for prime or not            
def is_prime(n):
    count=0
    if n==0 or n==1:
        return False
    else:
        for i in list_of_prime: #checks for the divisibility with just the prime number less than the number.
            if n%i==0:
                count+=1
        if count>0:
            return False
            
        else:
            list_of_prime.append(n)
            return True
        


list_of_prime=[2]
max_index=6
index=1
number=1
while index<max_index:
    number+=2
    if is_prime(number):
        index+=1
        print 'the prime number of index & number',index,number
        

print '10001st prime number is',number  