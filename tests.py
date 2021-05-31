import os
from app.utils.cobmination import save_txt, save_xlxs, res


def test_save_xlxs():
    test_res = ['a1', 'a2', 'a3']
    name, time = save_xlxs(test_res)
    path = name + '.xlsx'
    assert os.path.exists(path)
    os.remove(path)


def test_save_txt():
    res = ['a1', 'a2', 'a3']
    name = 'testtime'
    save_txt(res, name)
    assert os.path.exists('testtime.txt')
    os.remove('testtime.txt')


def test_res():
    datas = {"a": 3, "b": 2}
    exc_set = {"a1": ["b2"]}
    name = res(datas, exc_set)
    path_xlsx = name + '.xlsx'
    path_txt = name + '.txt'
    assert os.path.exists(path_xlsx)
    assert os.path.exists(path_txt)
    os.remove(path_xlsx)
    os.remove(path_txt)
