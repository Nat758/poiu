# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

a=int(input('a= '))
if a==1:
    print('Первая четверть: x from 0 to + ∞, y from 0 to + ∞')
elif a==2:
    print('Вторая четверть: x from 0 to - ∞, y from 0 - ∞') 
elif a==3:
    print('Третья четверть: x from 0 to - ∞, y from 0 to - ∞')
elif a==4:
    print('Чуевертая четверть: x from 0 to + ∞, y from 0 to - ∞')
else:
    print('Error:  1<a<5')               



