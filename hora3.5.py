print("bem-vindo")
def teste():
    x=input("horas trabalhadas")
    try:
        x = float(x)
    except:
        print("favor digite um numero")
        quit()
    y=input("valor da hora de servico")
    try:
        y= float(y)
    except:
        print("favor digite um numero")
        quit()
teste()
print(x , y)
xy= x*y
print("seu salario do dia e" , xy ,"reais")
    
    
