'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('task3.txt', 'r') as file:
    saldo = []
    poor = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        saldo.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, saldo)) / len(saldo)}')
