salario = int(input('Qual o seu salario: '))

if salario > 1250:
    print ("Seu novo salario: %d " % (salario*1.1))
if salario <= 1250:
    print ("Seu novo salario: %d " % (salario*1.15))
