
import os
import numpy as np

def exibir_menu():
    
    print('CALCULADORA \n')

    print('Operações\n')
    
    print('1.Adição')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisão')
    print('5.Potenciação')
    print('4.Radiciação')

def definir_opcao():   
    try:
        opcao_escolhida = int(input('Selecione a operação que deseja realizar: \n'))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            adicao()
        elif opcao_escolhida == 2:
            subtracao()
        elif opcao_escolhida == 3:
            multiplicacao('Ativar restaurantes')
        elif opcao_escolhida == 4:
            divisao()
        elif opcao_escolhida == 5:
            potenciacao()
        elif opcao_escolhida == 6:
            radiciacao()
        elif opcao_escolhida == 7:
            mmc()    
        elif opcao_escolhida == 8:
            mdc()
                
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opção Invalida\n')
    Retornar_menu()
    
def adicao():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número que deseja somar ao primeiro\n'))
    
    soma_result = num1 + num2
    print(f'Resultado: {soma_result}')
    
def subtracao():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número que deseja subtrair do primeiro \n'))
    
    sub_result = num1 - num2
    print(f'Resultado: {sub_result}')    
    
def multiplicacao():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número que deseja multiplicar pelo primeiro \n'))
    
    mul_result = num1 * num2
    print(f'Resultado: {mul_result}')    
    
def divisao():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número que deseja dividir pelo primeiro \n'))
    
    div_result = num1 / num2
    print(f'Resultado: {div_result}')

def potenciacao():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número da potênciação \n'))
    
    pot_result = num1 ** num2
    print(f'Resultado: {pot_result}')
    
def radiciacao():
    num1 = int(input('Digite o número a ser radiciado \n'))
    num2 = int(input('Digite o indíce da radiciação \n'))
    
    raiz = np.nthroot(num1,num2)
    print(f'Resultado: {raiz}')

def mmc ():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número da radiciação \n'))
    
    soma_result = num1 // num2
    print(f'Resultado: {soma_result}')

def mdc():
    num1 = int(input('Digite o primeiro número \n'))
    num2 = int(input('Digite o número da radiciação \n'))
    
    soma_result = num1 // num2
    print(f'Resultado: {soma_result}')
          
def Retornar_menu():
    input('Aperte qualquer tecla para retornar ao menu principal: \n')
    main()
    
def main():
    os.system('cls')
    exibir_menu()
    definir_opcao()

if __name__ == '__main__':
    main()   
