def calcul_polynome(coefficients, nombre_de_coefficients, x):
    Resultat = coefficients[0]
    for i in range(1, nombre_de_coefficients):
        Resultat = Resultat*x + coefficients[i]
    return Resultat

def afficher_fonction(nombre_de_coefficients, liste_coefficients):
    Degre = nombre_de_coefficients - 1
    AfficherFonction = ""
    for coefficient in liste_coefficients:
        if Degre == 0:
            if coefficient != 0:
                AfficherFonction += str(coefficient)
        elif Degre == 1:
            if coefficient == 1:
                AfficherFonction += "x + "
            elif coefficient == 0:
                AfficherFonction += ""
            else:
                AfficherFonction += str(coefficient) + "x + "
        else:
            if coefficient == 1:
                AfficherFonction += "x^" + str(Degre) + " + "
            elif coefficient == 0:
                AfficherFonction += ""
            else:
                AfficherFonction += str(coefficient) + "x^" + str(Degre) + " + "
        Degre -= 1
    print("Donc la fonction f(x,t) =", AfficherFonction)
