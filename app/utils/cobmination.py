import os, os.path
from itertools import product
from openpyxl import Workbook
import datetime

dir_name = os.path.join(os.getcwd(), 'app/static/combs')

try:
    os.mkdir(dir_name)
    print("Directory ", dir_name, " Created ")
except FileExistsError:
    print("Directory ", dir_name, " already exists")


def res(datas, exc_set):
    # Инициализируем данные
    result = []
    max_var = max(datas.values())
    test_list1 = [x for x in datas]
    test_list2 = [str(i) for i in range(1, max_var + 1)]

    # using zip() + product() Создаем все комбинации по максимальному элементу
    res = list(list(zip(test_list1, ele)) for ele in product(test_list2, repeat=len(test_list1)))

    # Соединяем параметры и номера в строки
    res2 = []
    for i in res:
        tmp = [x + y for (x, y) in i]
        res2.append(tmp)

    # удаляем комбинации с лишними элементами
    exc = []
    for key in datas:
        if datas[key] < max_var:
            for i in range(datas[key] + 1, max_var + 1):
                exc.append(key + str(i))
    res3 = []
    for comb in res2:
        exc_bool = [x in comb for x in exc]
        if any(exc_bool):
            continue
        else:
            res3.append(comb)

    # удаляем комбинации с исключениями
    if exc_set:
        for comb in res3:
            if any([x in comb for x in exc_set]):
                exc = []
                for par in exc_set:
                    if par in comb:
                        exc += exc_set[par]

                ecx_set_bool = [x in comb for x in exc]
                if any(ecx_set_bool):
                    continue
                else:
                    result.append(comb)
            else:
                result.append(comb)
    else:
        result = res3

    name, time = save_xlxs(result)
    save_txt(result, name)
    return name


# сохраняем данные в формате xlsx
def save_xlxs(res):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Комбинации'
    for row in range(len(res)):
        for col in range(len(res[0])):
            _ = ws.cell(column=col + 1, row=row + 1, value=res[row][col])
    time = datetime.datetime.now().strftime('%H%M%S')
    name = f'combination-{time}'
    wb.save(f'{name}.xlsx')
    return name, time


def save_txt(res, name):
    with open(f'{name}.txt', 'w') as f:
        f.write('Существуют следующие комбинации:\n')
        for line in res:
            comb = ','.join(line)
            f.write(comb + '\n')


def moving_to_dir(name):
    basedir = os.getcwd()
    name_xlsx = name + '.xlsx'
    name_txt = name + '.txt'
    path1 = os.path.join(basedir, 'app/static/combs', name_xlsx)
    os.system(f'mv {name_xlsx} {path1}')
    path2 = os.path.join(basedir, 'app/static/combs', name_txt)
    os.system(f'mv {name_txt} {path2}')
