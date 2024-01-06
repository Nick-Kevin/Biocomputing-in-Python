from compute_polynomial_equation import calcul_polynome

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
