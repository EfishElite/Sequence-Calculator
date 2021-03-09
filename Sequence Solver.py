import random as rd
import time as time

def cubicSequence():
    a = rd.randint(1,25)
    b = rd.randint(1,25)
    c = rd.randint(1,25)
    d = rd.randint(1,25)

    n = 1

    while n!=6:
        sequence1 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence2 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence3 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence4 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence5 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
    if n == 6:
        print ("Sequence:", sequence1, sequence2, sequence3, sequence4, sequence5)


def quadSequence():
    a = rd.randint(1,25)
    b = rd.randint(1,25)
    c = rd.randint(1,25)

    n = 1

    while n!=7:
        sequence1 = a*n**2 + b*n + c
        n = n + 1
        
        sequence2 = a*n**2 + b*n + c
        n = n + 1
        
        sequence3 = a*n**2 + b*n + c
        n = n + 1
        
        sequence4 = a*n**2 + b*n + c
        n = n + 1

        sequence5 = a*n**2 + b*n + c
        n = n + 1

        sequence6 = a*n**2 + b*n + c
        n = n + 1


    if n == 7:
        print ("Sequence:", sequence1, sequence2, sequence3, sequence4, sequence5, sequence6)


def geometric():

    n = 1

    r = rd.randint(2, 7)

    a = r

    n = n + 1
    
    sequence1 = a*r**(n-1)
    n = n + 1

    sequence2 = a*r**(n-1)
    n = n + 1

    sequence3 = a*r**(n-1)
    n = n + 1

    sequence4 = a*r**(n-1)
    n = n + 1
 
    if n == 6:
        print ("Sequence:", a, sequence1, sequence2, sequence3, sequence4)

def fibonacci():
    nterms = int(input("How many terms? "))
    
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1


while True:
    print("This will calculate an+b sequences, quadratics, any value in a fibonacci sequence, and cubic sequences")
    time.sleep(3)
    
    sequence = input("A: Quadratic, B: Cubic, C: Geometric, D: Fibonacci")

    if sequence == "A".lower():
        quadSequence()
        time.sleep(5)
        
    elif sequence == "B".lower():
        cubicSequence()
        time.sleep(5)

    elif sequence =="C".lower():
        geometric()
        time.sleep(5)
        
    elif sequence == "D".lower():
        fibonacci()
        time.sleep(5)
        
    else:
        print ("Enter a valid input")
