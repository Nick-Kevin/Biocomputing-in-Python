from compute_polynomial_equation import calcul_polynome, afficher_fonction

def calcul_pas_de_reccurence(intervalle, sous_intervalles):
    a = intervalle[0]
    b = intervalle[1]
    n = sous_intervalles
    h = (b-a)/n
    return h

def euler(intervalle, sous_intervalles, liste_coefficients):
    a = intervalle[0]
    n = sous_intervalles
    x = []
    x.append(a)
    h = calcul_pas_de_reccurence(intervalle, sous_intervalles)
    NombreDeCoefficients = len(liste_coefficients)
    for k in range(n):
        NouveauX = x[k] + h*calcul_polynome(liste_coefficients, NombreDeCoefficients, x[k])
        x.append(NouveauX)
    print("\nSolution approchée")
    NumeroDeX = 0
    for i in x:
        print("x" + str(NumeroDeX) + ":", i)
        NumeroDeX += 1
    return x[len(x)-1]

def principale():
    NombreDeCoefficients = int(input("\nPour la fonction f(x,t)\nEntrez le nombre de coefficients: "))
    CoefficientsDeLaFonction = []
    Degre = NombreDeCoefficients - 1
    for i in range(NombreDeCoefficients):
        Coefficient = int(input("Enter the coefficient for x^"+str(Degre)+": "))
        CoefficientsDeLaFonction.append(Coefficient)
        Degre -= 1
    print("Pour l'interval [a,b]")
    Intervalle = []
    a = int(input("Entrez a: "))
    Intervalle.append(a)
    b = int(input("Entrez b: "))
    Intervalle.append(b)
    NombreDeSousIntervalle = int(input("Entrez le nombre de sous-intervalles: "))
    print()
    afficher_fonction(NombreDeCoefficients, CoefficientsDeLaFonction)
    print("L'intervalle [a,b] est:", Intervalle)
    print("Le nombre de sous-intervalles n est:", NombreDeSousIntervalle)
    euler(Intervalle, NombreDeSousIntervalle, CoefficientsDeLaFonction)

principale()
