
def printPol(pol):
    polFinal = ""
    for i in range(1, len(pol)):
        stringAux = str(pol[i])
        polFinal += (stringAux + "X^" + str(i)+ " + ")
    polFinal += str(pol[0])
        
    return polFinal


def somarPolinomio(pol1, pol2):
    #confere se existe alguma diferença de grau entre os polinômios,
    #checando o maior grau de expoente em cada um dos dois, salvando em uma variável
    #para ser usada posteriormente no processo da soma 
    dif = pol1[len(pol1) - 1][1] - pol2[len(pol2) - 1][1]
    #checa se um polinômio é maior do que o outro, se a dif for > 0 o pol1 é maior, se for < 0 o pol2 é maior
    #se dif == 0 então ele faz a soma normalmente
    if dif > 0 or dif < 0:
        #confere o tamanho do menor polinômio pelo grau e cria um novo vetor a partir do tamanho do maior
        if pol1[len(pol1) - 1][1] < pol2[len(pol2) - 1][1]:
            #vetor que recebe o polinômio resultante da soma, ele usa o tamanho do maior 
            #polinômio.
            polSoma = [0]*(pol2[len(pol2)-1][1] + 1)
            #loop para somar os valores de expoentes iguais
            for g in range(pol1[len(pol1) - 1][1] + 1):
                polSoma[g] = pol1[g][0] + pol2[g][0]
            #loop para adicionar ao vetor que recebe ao polinômio os valores que não seriam somados
            #ou seja, aqueles que ficaram fora da soma acima
            for l in range(pol1[len(pol1) - 1][1]+1, pol2[len(pol2) - 1][1]+1):
                polSoma[l] = pol2[l][0]
            return polSoma
        else:
            #vetor que recebe o polinômio resultante da soma, ele usa o tamanho do maior 
            #polinômio.
            polSoma = [0]*(pol1[len(pol1)-1][1] + 1)
            #loop para somar os valores de expoentes iguais
            for g in range(pol2[len(pol2) - 1][1] + 1):
                polSoma[g] = pol1[g][0] + pol2[g][0]
            #loop para adicionar ao vetor que recebe ao polinômio os valores que não seriam somados
            #ou seja, aqueles que ficaram fora da soma acima
            for l in range(pol2[len(pol2) - 1][1] + 1, pol1[len(pol1) - 1][1] + 1):
                polSoma[l] = pol1[l][0]
            return polSoma
    else:
        polSoma = [0]*(pol1[len(pol1)-1][1] + 1)
        for g in range(pol1[len(pol1)-1][1]+1):
            polSoma[g] = pol1[g][0] + pol2[g][0]
        return polSoma

def multPol(pol1, pol2):
  tamanho = (len(pol1)*len(pol2))
  mat = [None] * tamanho
  for l in range(tamanho):
    mat[l] = [0]* 2
  h = 0
  for i in range(len(pol1)):
    for g in range(len(pol2)):
      mat[h][0] = pol1[i][0]*pol2[g][0]
      mat[h][1] = pol1[i][1]+pol2[g][1]
      h += 1
  aux = ((pol1[len(pol1)-1][1]+pol2[len(pol2)-1][1])+1) *[0]
  for i in range(len(aux)):
    for g in range(len(mat)):
      if i == mat[g][1]:
        aux[i] += mat[g][0]
  return aux

def calcX(pol, x):
  soma = 0
  for i in range(len(pol)):
    soma += (pol[i][0])*(x**pol[i][1])
  return soma

def main():
  opc = 0
  while opc != 4:
    print("\nEscolha entre as opções abaixo \n\n1-Calcule o valor do polinômio \n2-Calcular a soma dos polinômios \n3-Calcular a multiplicação dos Polinômios \n4-Encerrar programa")
    opc = int(input())
    if opc == 1:
      y = float(input("Digite o valor de x: "))
      polinomio = [0] * 1
      for h in range(1): #ler o polinomio
        grau = int(input("\n Digite o grau do polinomio : "))
        poli = [0] * (grau + 1)
        t = 0
        for i in range(grau + 1):
          ele = [0] * 2
          if i == 0:
            coef = float(input("\nDigite o termo independente"))
          if i > 0 :
            coef = float(input("\nDigite o Coeficiente: "))
          ele[0] = coef
          ele[1] = t
          poli[i] = ele
          t += 1
        polinomio[h] = poli
      valores = calcX(polinomio[0], y)
      print("P({:.0f}) = {}".format(y, valores))
    if opc == 2:
      polinomio = [0] * 2
      for h in range(2): #ler o polinomio
        grau = int(input("\n Digite o grau do polinomio {}: ".format(h+1)))
        poli = [0] * (grau + 1)
        t = 0
        for i in range(grau + 1):
          ele = [0] * 2
          if i == 0:
            coef = float(input("\nDigite o termo independente:"))
          if i > 0 :
            coef = float(input("\nDigite o Coeficiente: "))
          ele[0] = coef
          ele[1] = t
          poli[i] = ele
          t += 1
        polinomio[h] = poli
      soma = somarPolinomio(polinomio[0], polinomio[1])
      print(printPol(soma))
    if opc == 3:
      polinomio = [0] * 2
      for h in range(2): #ler o polinomio
        grau = int(input("\n Digite o grau do polinomio {}: ".format(h+1)))
        poli = [0] * (grau + 1)
        t = 0
        for i in range(grau + 1):
          ele = [0] * 2
          if i == 0:
            coef = float(input("\nDigite o termo independente: "))
          if i > 0 :
            coef = float(input("\nDigite o Coeficiente: "))
          ele[0] = coef
          ele[1] = t
          poli[i] = ele
          t += 1
        polinomio[h] = poli
      res = multPol(polinomio[0],polinomio[1])
      print(printPol(res))
    if opc == 4:
      break


# Run
main()
