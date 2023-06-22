while True:
 primeiro_numero = int(input("digite o primeiro número: "))
 if primeiro_numero == 0:
    break   
 
 operacao = input("")
 segundo_numero = int(input('digite o segundo número: '))
 if operacao == "+":
    resultado = primeiro_numero + segundo_numero
    print('resultado é', resultado)
 elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
    print('resultado é', resultado)
 elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
    print('resultado é', resultado)   
 elif operacao == "/":
    resultado = primeiro_numero / segundo_numero
    print('resultado é',resultado)    
 else:
    print('digite uma operação válida')  

 print('\n')   
