def horner(coefficients, coefficients_number, x):
    Result = coefficients[0]
    for i in range(1, coefficients_number):
        Result = Result*x + coefficients[i]
    return Result

def display_function(number_of_coefficients, coefficients_list):
    Degree = number_of_coefficients - 1
    TheFunction = ""
    for coefficient in coefficients_list:
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
