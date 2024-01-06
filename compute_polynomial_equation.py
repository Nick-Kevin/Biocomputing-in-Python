def calcul_polynome(coefficients, nombre_de_coefficients, x):
    Resultat = coefficients[0]
    for i in range(1, nombre_de_coefficients):
        Resultat = Resultat*x + coefficients[i]
    return Resultat

X = 3
Coefficient = [2, -6, 2, -1]
CoefficientsNumber = len(Coefficient)

print(calcul_polynome(Coefficient, CoefficientsNumber, X))
