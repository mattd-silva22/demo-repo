print("bem-vindo")
def teste():
    hora_trabalho = input("horas trabalhadas")
    try:
    hora_trabalho = float(x)
    except:
        print("favor digite um numero")
        quit()
    valor_hora = input("valor da hora de servico")
    try:
        valor_hora = float(y)
    except:
        print("favor digite um numero")
        quit()
salario_dia = hora_trabalho * valor_hora
print("seu salario do dia e" , salario_dia ,"reais")
    
    
