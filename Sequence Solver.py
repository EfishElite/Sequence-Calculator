import random as rd
import time as time


def nSolver():
    x = s1 - dif1
    
    if x > 0:
        print ("Sequence:", dif1, "n +", x)
    elif x < 0:
        print ("Sequence:", dif1, "n", x)
    else:
        print ("Sequence:", dif1, "n")


def qSolver():
    if dif1a == 2 and dif1b == 2:
        a = 1
        print ("A:", a)
        n = 1
        r1 = s1 - n**2
        n = n + 1
        r2 = s2 - n**2
        n = n + 1
        r3 = s3 - n**2
        n = n + 1
        r4 = s4 - n**2
        n = n + 1
        r5 = s5 - n**2
        diff1 = r2 - r1
        b = diff1
        print ("B:", b)
        c = r1 - b
        print ("C:", c)
        
    elif dif1a!=2:
        a = dif1a/2
        print ("A:", a)
        n = 1
        r1 = s1 - a*(n**2)
        n = n + 1
        r2 = s2 - a*(n**2)
        n = n + 1
        r3 = s3 - a*(n**2)
        n = n + 1
        r4 = s4 - a*(n**2)
        n = n + 1
        r5 = s5 - a*(n**2)
        diff1 = r2 - r1
        b = diff1
        print ("B:", b)
        c = r1 - b
        print ("C:", c)

def geometric():
    a = s1
    r = s2/s1
    n = int(input("Enter the location of the number:"))
    location = n-1
    answer1 = r**location
    answer = answer1*a
    print (answer)


def cubicSolver():
    a = dif2a/6
    print ("A:", a)
    b = dif1a - 12*a
    b = b/2
    print ("B:", b)
    c = s2 - s1 - 7*a - 3*b
    print ("C:", c)
    d = 4 - a - b - c
    print ("D:", d)
    

while True:
    s1 = int(input("Enter number 1:"))
    s2 = int(input("Enter number 2:"))
    s3 = int(input("Enter number 3:"))
    s4 = int(input("Enter number 4:"))
    s5 = int(input("Enter number 5:"))


    dif1 = s2 - s1
    dif2 = s3 - s2
    dif3 = s4 - s3
    dif4 = s5 - s4

    dif1a = dif2 - dif1
    dif1b = dif3 - dif2
    dif1c = dif4 - dif3

    dif2a = dif1b - dif1a
    dif2b = dif1c - dif1b
    
    if dif1 == dif2:
        nSolver()
        
    elif dif1a == dif1b and dif1b == dif1c:
        qSolver()

    elif s1 == s2/2 or s1 == s2/3 or s1 == s2/4 or s1 == s2/5:
        geometric()

    elif dif2a == dif2b:
        cubicSolver()
        
    else:
        print ("Enter correct numbers:")
