tickets=int(input('Сколько билетов необходимо преобрести? '))
HowOld = [int(input('Введите возраст посетителя ')) for i in range(tickets)]
summ=0
for i in range(tickets):
    if 18 <= HowOld[i] <25 :
        summ +=990
    elif HowOld[i]>=25 :
        summ +=1390
if tickets>3 :
    summ-=summ*0.1
    print (f'Всего к оплате со скидкой {summ} ')
else: print (f'Всего к оплате  {summ} ')
