from compute_polynomial_equation import horner, display_function

def calculate_reccurence_step(interval, subintervals):
    a = interval[0]
    b = interval[1]
    n = subintervals
    h = (b-a)/n
    return h

def euler(interval, subintervals, coefficients):
    a = interval[0]
    n = subintervals
    x = []
    x.append(a)
    h = calculate_reccurence_step(interval, subintervals)
    CoefficientsNumber = len(coefficients)
    for k in range(n):
        NewX = x[k] + h*horner(coefficients, CoefficientsNumber, x[k])
        x.append(NewX)
    for i in x:
        print(i)
    return x[len(x)-1]

def main():
    NumberOfCoefficients = int(input("\nFor the f(x,t) function\nEnter the number of coefficients: "))
    CoefficientsOfTheFunction = []
    Degree = NumberOfCoefficients - 1
    for i in range(NumberOfCoefficients):
        Coefficient = int(input("Enter the coefficient for x^"+str(Degree)+": "))
        CoefficientsOfTheFunction.append(Coefficient)
        Degree -= 1    
    print("For the [a,b] interval")
    Interval = []
    a = int(input("Enter a: "))
    Interval.append(a)
    b = int(input("Enter b: "))
    Interval.append(b)
    SubintervalsNumber = int(input("Enter the number of subintervals: "))
    print()
    display_function(NumberOfCoefficients, CoefficientsOfTheFunction)
    print("The [a,b] interval is:", Interval)
    print("The number of subintervals n is:", SubintervalsNumber)
    euler(Interval, SubintervalsNumber, CoefficientsOfTheFunction)

main()
