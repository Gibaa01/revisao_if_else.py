
#repeticao usando for in

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""for num in numeros :
    print(num)

for num in range (1,101):   # range cria lista de numeros 
    if(num %2 ==0):
        print(num)


#interando sobre uma string

for letras in "Giovanni":
    print(letras)
    
#repeticao usando while 

soma =0

numeros = range(1,1000)

i=0

while soma < 100:
    soma += numeros[i]
    i +=1
print(soma)


x = 0

while x < 5 :
    print("valor de x:", x)
    print(" x ainda e maior do que 5 vamos somar 1")
    x +=1
else:
    print("fim")
    
  
#break: parar o loop
#continue: proximo loop 
#pass:nao faz nada

soma = 0
x = 0

while x < 1000 :
    x+=1
    if x%3==0:
        print(x)
        soma+=x
    else :
        if x%5==0:
            pass
        else:
            print("buscando...")
            continue
    if soma >300:
        print(soma)
        break
        """
        
        
        
#desafio 1 num1 = int(input("digite um numero para saber sua tabuada "))

#for i in range(1,11) :
#    print(num1 ,"x", i, "=", num1 *i)


#desafio 2



valores = []

for i in range(10):
    num=int(input(f"digite o {i+1} numero:"))
    valores.append(num)
    
    
maior = valores [0]
posicao = 0

for i in range(10):
    if valores[i] > maior:
        maior = valores[i]
        posicao = i

print("maior valor", maior)
print("posicao",posicao)