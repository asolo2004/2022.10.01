# Т.к не было оговорено в каком виде выводить ответ, использую float
a = int(input('Введите первый катет:'))
b = int(input('Введите второй катет:'))
print('Площадь: '+str(a*b/2))
print('Периметр: '+str((a*a+b*b)**0.5+a+b))
