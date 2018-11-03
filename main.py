import Calculadora as calculadora

if __name__ == '__main__':

    while True:

        print('--------------------------------------------')
        print('----------------CALCULADORA-----------------')
        print('--------------------------------------------')
        print('Seleccione la operación a realizar: ')
        print('1 - Sumar ')
        print('2 - Restar ')
        print('3 - Dividir ')
        print('4 - Multiplicar ')
        print('5 - Salir ')
        print('-------------------------------------------- ')
        print('-------------------------------------------- ')

        opcion = input("Opción: ")

        try:
            int(opcion)
        except:
            print('La opción debe ser un dígito')
        else:    
            if int(opcion) == 5:
                break
            else:
                valor1 = input("Ingrese el valor 1: ")
                valor2 = input("Ingrese el valor 2: ")    
                print('El resultado es: ', calculadora.switch(int(opcion), int(valor1), int(valor2)))
