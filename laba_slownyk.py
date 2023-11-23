order={}
money=0
print('ви прийшли у ресторан і готові віддати все щоб добре поїсти')
order['імя']=input('імя:\n')
age=int(input('ваш вік:\n'))
order['сніданок']=input('головне:\n')
if age >= 4:
    order['обід']=input('друге:\n')
order['вечерю']=input('десерт:\n')
print('всього з вас:')
for i in order:
     money=money+len(order[i])
print(money , 'грн')
order['вік'] = age
print('ваше замовлення:',order)