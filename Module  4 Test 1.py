f= int(input('Enter a number: '))
def factorial(f):
    if f<2:
        return 1
    else:
        return(f*factorial(f-1))
print('factorial of ',f,' is: ',factorial(f))
