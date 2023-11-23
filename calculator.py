num1=float(input('введіть номер:'))
num2=float(input('введіть інший номер:'))
operation=input('що саме зробити?')
if operation == '+':    #додавання
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
elif operation == '-':  #віднімання
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)
elif operation == '*':  #множення
    print ('{} * {} = '.format(num1, num2))
    print (num1 * num2)
elif operation == '/':  #ділення
    if num2==0:  #помилка
        print('на нуль ділити не можна')
    else:
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)
else:
    print('щось пішло не так, спробуйте ще раз.')