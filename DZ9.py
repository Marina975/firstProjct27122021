print('Тодорова Марина')
print('Cделать конвертер валют')
print('_________________________________________________\n')

from DZ9classEUR import Euro
from DZ9classRUB import Rubl
from DZ9classUSD import Dollar

flag = True
while flag == True:
    print('Для конвентирования выберите тип валюты, в которую Вы хотите перевести тенге\n')
    print('Введите цифру от 1 до 3, где: \n \t1 - Евро \n \t2 - Российский рубль \n \t3 - Американский доллар \n \t')

    viborValuti = int(input('\t\t'))
    if viborValuti >=1 and viborValuti <4:
        flag = False

    summaKObmenu = int(input('\nВведите сумму денег, в тенге: '))
    
    if viborValuti == 1:
        euroKonvert = Euro()
        result_konvert = euroKonvert.konvert(summaKObmenu)
        print(f'\nКонвентированная сумма составляет: {int(result_konvert)} евро')
    elif viborValuti == 2:
        rublKonvert = Rubl()
        result_konvert = rublKonvert.konvert(summaKObmenu)
        print(f'\nКонвентированная сумма составляет: {int(result_konvert)} рублей')
    elif viborValuti == 3:
        dollarKonvert = Dollar()
        result_konvert = dollarKonvert.konvert(summaKObmenu)
        print(f'\nКонвентированная сумма составляет: {int(result_konvert)} долларов')
    else:
        print('Вы ввели что-то не то...')




