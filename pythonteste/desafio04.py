var = input("digite algo ")
tipo = type(var)
space = var.isspace()
num = var.isnumeric()
alf = var.isalpha()
alfnum = var.isalnum()
maius  = var.isupper()
minus = var.islower()
cap = var.istitle()

print("digite algo: {} \nO tipo primitivo é: {} \nTem espaços? {} \nÈ numérico? {} \nÉ alfabético? {} \nÉ alfanumérico? {} \nEstá em maiúsculas? {} \nEstá em minusculas? {} \nEsta capitalizada?{} "
      .format(var, tipo, space, num, alf, alfnum, maius, minus, cap))