peso = float(input("Coloque o seu peso: "))
altura = float(input("Coloque a sua altura: "))

IMC = peso / (altura ** 2) 

print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif IMC >= 18.5:
    print("Você está com o peso normal.")
elif IMC < 25:
    print("Você esta sobrepeso")


#De inicio , a ideia programa é desenvolver uma maneira mais rapida de se calcular o seu IMC ,
#os metodos que utilizei foram FLOAT na questão em que o PESO e a ALTURA não são numeros inteiros assim , 
#faz mais sentido usar FLOAT do que o INT nessa ocasião , tambem utilizei o IF e ELIF , para que dependendo do resultado a pessoa saiba se esta acima ou abaixo do peso ideial para si .
#Os resultado foram dentro do esperado, ja que é um calculo simples e facil de se desenvolver .
