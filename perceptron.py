import treinarCaractere as train
import testesDistorcidos as testes

class Perceptron:

    def __init__(self, limiar, w):
        self.limiar = limiar
        self.w = w
        self.eta = 0.2

    def treinar(self, vetorCarctere, desejado):
        gerado = self.definirSaida(vetorCarctere)

        if gerado == desejado:
            return True
        else:
            self.atualizar(vetorCarctere, desejado, gerado)
            return False
    
    def definirSaida(self, vetorCaractere):
        j = 0
        x = [i for i in vetorCaractere]
        resultado = 1*(self.limiar*(-1))
        
        for x in x:
            resultado = resultado + (x*self.w[j])
            j += 1
            
        return 1 if resultado >= 0 else -1

    def atualizar(self, vetorCaractere, desejado, gerado):
        for i in range(len(self.w) - 1):
            self.w[i] = self.w[i] + (self.eta*(vetorCaractere[i])*(desejado - (gerado)))
            if (i == 0):
                self.limiar = self.w[i]*1


w = [0.4, 0.5, 0.2, 0.7, 0.8, 0.6, 0.3, 0.9, 0.1, 0.4]
perceptron = Perceptron(0.5, w)
t = train.Treinar.T
h = train.Treinar.H

contador = 0

while (contador < 2):
    if (perceptron.treinar(t, 1) == True):
        contador += 1

    if (perceptron.treinar(h, -1) == True):
        contador += 1


##         ##
##  SAÍDA  ##   
##         ##
linha = "============================================================================="

print('{:>40}'.format('Teste para T'))
print(linha)
print("Para o teste: ", t, "\n"
      "Resultado gerado é: ", perceptron.definirSaida(t), "\n")

if (perceptron.definirSaida(t) == 1):
    print("Resultado gerado é igual ao esperado.")
else:
    print("Resultado gerado é diferente do esperado.,")

print(linha,"\n")
print('{:>40}'.format('Teste para H'))
print(linha)
print("Para o teste: ", h, "\n"
      "Resultado gerado é: ", perceptron.definirSaida(h), "\n")

if (perceptron.definirSaida(h) == -1):
    print("Resultado gerado é igual ao esperado.")
else:
    print("Resultado gerado é diferente do esperado.")


# Testes para T distorcido
teste1 = testes.TestesDistorcidos.teste1
teste2 = testes.TestesDistorcidos.teste2
teste3 = testes.TestesDistorcidos.teste3

# Testes para H distorcido
teste4 = testes.TestesDistorcidos.teste4
teste5 = testes.TestesDistorcidos.teste5
teste6 = testes.TestesDistorcidos.teste6

print(linha,"\n")
print('{:>50}'.format('Testes distorcidos para T'))
print(linha,"\n")
print("Para o teste 1: ", teste1, "\n"
      "Resultado gerado é: ", perceptron.definirSaida(teste1), "\n"
      "\n"
      "Para o teste 2: ", teste2, "\n"
      "O resultado gerado é: ", perceptron.definirSaida(teste2), "\n"
      "\n"
      "Para o teste 3: ", teste3, "\n"
      "O resultado gerado é: ", perceptron.definirSaida(teste3)
      )

print(linha,"\n")
print('{:>50}'.format('Testes distorcidos para H'))
print(linha)
print("Para o teste 1: ", teste4, "\n"
      "Resultado gerado é: ", perceptron.definirSaida(teste4), "\n"
      "\n"
      "Para o teste 2: ", teste5, "\n"
      "O resultado gerado é: ", perceptron.definirSaida(teste5), "\n"
      "\n"
      "Para o teste 3: ", teste6, "\n"
      "O resultado gerado é: ", perceptron.definirSaida(teste6)
      )
print(linha)
