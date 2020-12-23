#Calculadora de Valor Presente, Valor Futuro e Taxa de Retorno [JUROS SIMPLES]

print()
print("Calculadora de Valor Presente, Valor Futuro ou Taxa de Retorno")
print()
print("Painel de seleção:")
print("1 - Valor Presente")
print("2 - Valor Futuro")
print("3 - Taxa de Retorno")
print()

n = int(input("Insira o número do fator que deseja calcular: "))

if n == 1:
    VF = float(input("Qual é o Valor Futuro? "))
    I = float(input("Qual é a taxa de retorno em %? (Insira o valor com ponto ao invés de vírgula) "))
    T = float(input("Qual é o tempo de aplicação? "))
    print()
    VP = float(VF/(1+(I/100*T)))
elif n == 2:
    VP = float(input("Qual é o Valor Presente? "))
    I = float(input("Qual é a taxa de retorno em %? (Insira o valor com ponto ao invés de vírgula) "))
    T = float(input("Qual é o tempo de aplicação? "))
    VF = float(VP*(1+(I/100*T)))
    print()
    print("O Valor Futuro é: ", VF)
elif n == 3:
    VP = float(input("Qual é o Valor Presente? "))
    VF = float(input("Qual é o Valor Futuro? "))
    T = float(input("Qual é o tempo de aplicação? "))
    I = float((VF/VP - 1)/T)
    print()
    print("A taxa de retorno do período é: ", I, "%")