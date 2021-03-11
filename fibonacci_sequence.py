# Given a Fibonacci sequence that contains the integer sequence of 0, 1, 1, 2, 3, 5, 8....

# You will be asked to display Fibonacci sequence using a recursive function. Any forms of coding languages (Py, R, C++, C#, even pseudocode) are allowed. 

def fibbo(n):
    n1, n2 = 1, 2
    print(n1,n2,end=' ')
    for i in range(3,n):
        fibbo = n1 + n2
        print(fibbo,'',end='')
        n1 = n2
        n2 = fibbo
    print('')
    return

n = int(input())

fibbo(n)