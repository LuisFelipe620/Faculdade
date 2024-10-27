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



