valid_input = True

try:
    target_ip = string(input("Introduce la ip de la máquina objetivo. También puedes incluir el nombre: "))
    
    if operador in ['+', '-', '*', '/']:
        if operador == '+':
            resultado = M1 + M2
        elif operador == '-':
            resultado = M1 - M2
        elif operador == '*':
            resultado = M1 * M2
        elif operador == '/':
            if M2 != 0:
                resultado = M1 / M2
            else:
                print('Imposible dividir entre 0')
                valid_input = False        
    else:
        print ('Por favor introduce un operador válido')
        valid_input = False
except ValueError:
    print("Por favor, introduce un número.")
    valid_input = False

if valid_input == True:
    print ('El resultado es ' + str(resultado))


