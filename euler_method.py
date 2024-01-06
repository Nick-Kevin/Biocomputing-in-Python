from compute_polynomial_equation import calcul_polynome, afficher_fonction

def calcul_pas_de_reccurence(intervalle, sous_intervalles):
    a = intervalle[0]
    b = intervalle[1]
    n = sous_intervalles
    h = (b-a)/n
    return h

def euler(intervalle, sous_intervalles, coefficients, coefficients_number):
    a = intervalle[0]
    n = sous_intervalles
    x = []
    x.append(a)
    h = calcul_pas_de_reccurence(intervalle, sous_intervalles)
    for k in range(n):
        NouveauX = x[k] + h*calcul_polynome(coefficients, coefficients_number, x[k])
        x.append(NouveauX)
    for i in x:
        print(i)
    return x[len(x)-1]

def principale():
    NombreDeCoefficients = int(input("\nPour la fonction f(x,t)\nEntrez le nombre de coefficients: "))
    CoefficientsDeLaFonction = []
    Degre = NombreDeCoefficients - 1
    for i in range(NombreDeCoefficients):
        Coefficient = int(input("Enter the coefficient for x^"+str(Degre)+": "))
        CoefficientsDeLaFonction.append(Coefficient)
        Degre -= 1
    print()
    afficher_fonction(NombreDeCoefficients, CoefficientsDeLaFonction)

principale()
