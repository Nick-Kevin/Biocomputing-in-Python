from compute_polynomial_equation import horner

def calculate_reccurence_step(interval, subintervals):
    a = interval[0]
    b = interval[1]
    n = subintervals
    h = (b-a)/n
    return h

def euler(interval, subintervals, coefficients, coefficients_number):
    a = interval[0]
    n = subintervals
    x = []
    x.append(a)
    h = calculate_reccurence_step(interval, subintervals)
    for k in range(n):
        NewX = x[k] + h*horner(coefficients, coefficients_number, x[k])
        x.append(NewX)
    for i in x:
        print(i)
    return x[len(x)-1]

def main():
    NumberOfCoefficients = int(input("\nFor the f(x,t) function:\nEnter the number of coefficients: "))
    CoefficientsOfTheFunction = []
    Degree = NumberOfCoefficients - 1
    for i in range(NumberOfCoefficients):
        Coefficient = int(input("Enter the coefficient for x^"+str(Degree)+": "))
        CoefficientsOfTheFunction.append(Coefficient)
        Degree -= 1
    print()
    Degree = NumberOfCoefficients - 1
    TheFunction = ""
    for coefficient in CoefficientsOfTheFunction:
        if Degree == 0:
            if coefficient != 0:
                TheFunction += str(coefficient)
        elif Degree == 1:
            if coefficient == 1:
                TheFunction += "x + "
            elif coefficient == 0:
                TheFunction += ""
            else:
                TheFunction += str(coefficient) + "x + "
        else:
            if coefficient == 1:
                TheFunction += "x^" + str(Degree) + " + "
            elif coefficient == 0:
                TheFunction += ""
            else:
                TheFunction += str(coefficient) + "x^" + str(Degree) + " + "
        Degree -= 1
    print("So f(x,t) =", TheFunction)

main()
