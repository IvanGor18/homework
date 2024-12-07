x,y= map(float,input("Введите сначала делимое, потом делитель через пробел:").split())


if y ==0:
    print("Eррор вводи не ноль")

print(x/y)

##   2
inputsum = float(input("Введите сумму покупки: "))
    
if inputsum >= 20:
    d_sum = inputsum * 0.65
    discount = inputsum - d_sum
    r_discount = round(discount, 2)
    print(f"Сумма к оплате: {round(d_sum,2)} руб.")
    print(f"Размер скидки: {round(discount,2)} руб.")
else:
    print("Скидки не будет")
    
## 3 

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']

number = int(input("Введите число от 1 до 12: "))

if 1 <= number <= 12:
    x,y  = months[number - 1], seasons[number - 1]
else:
    print(f"Недопустимое значение. Введено число {number}")

print(f"{x}. {y}")