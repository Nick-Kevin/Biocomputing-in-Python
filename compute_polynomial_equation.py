def horner(coefficients, coefficients_number, x):
    Result = coefficients[0]
    for i in range(1, coefficients_number):
        Result = Result*x + coefficients[i]
    return Result

X = 3
Coefficient = [2, -6, 2, -1]
CoefficientsNumber = len(Coefficient)

print(horner(Coefficient, CoefficientsNumber, X))
