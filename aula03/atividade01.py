   # entrada
salario = float (input (' Informe o Salario :'))

#processamento
 

 percentual = float (input('informe o Digito para percentual:  '))
 percentual = percentual /100



subtotal = salario * percentual

total = subtotal +salario


# Saida
print (F' \n Salário Anterior : R${salario} ')
print(f' Valor do Reajuste : R$ {subtotal} ')
print(f' Novo Salario : R$ {total} ')