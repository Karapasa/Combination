from abc import ABC
from browser import document, html, bind, console, ajax, window
from browser.local_storage import storage
import json


_name = ''

try:
    storage['parlist']
    storage['exclist']
except:
    storage['parlist'] = json.dumps({})
    storage['exclist'] = json.dumps({})


class ABCcreator(ABC):
    def create_elem(self):
        pass


class ABCelement(ABC):

    def get_data(self):
        pass

    def add_el(self):
        pass

    def add_row(self):
        pass

    def _save(self):
        pass

    def remove(self):
        pass

    def clear_data(self):
        pass


class CreatParam(ABCcreator):
    def create_elem(self):
        return Param()


class CreateExc(ABCcreator):
    def create_elem(self):
        return Excep()


class Mixin:
    def create_row(self, par, second_cheet):
        row = html.TR(id=par)
        link = html.A('-', href='#')
        link.bind('click', self.remove)
        row <= html.TD(par) + html.TD(second_cheet) + html.TD(link)
        return row

    def remove_row(self, e):
        a = e.target.parent.parent
        del document[a.id]
        del self.elements[a.id]

    def remove_datas(self, datas):
        datas.clear()
        self.elements = {}
        self._save()


class Param(ABCelement, Mixin):

    def __init__(self):
        self.elements = json.loads(storage['parlist'])

    def get_data(self):
        par = document['name_parametr'].value
        quan = int(document['quantity_options'].value)
        return par, quan

    def add_el(self, e):
        par, quan = self.get_data()
        self.elements[par] = quan
        self._save()
        self.add_row(par)

    def add_row(self, par):
        second_cheet = self.elements[par]
        row = self.create_row(par, second_cheet)
        document['tbl_of_parametrs'].select('tbody')[0] <= row

    def _save(self):
        storage['parlist'] = json.dumps(self.elements)

    def remove(self, e):
        self.remove_row(e)
        self._save()

    def clear_data(self, e):
        datas = document['tbl_of_parametrs'].select('tbody')[0]
        self.remove_datas(datas)


class Excep(ABCelement, Mixin):
    def __init__(self):
        self.elements = json.loads(storage['exclist'])

    def get_data(self):
        par = document['name_par_exc'].value
        exc = document['exception_parametr'].value
        return par, exc

    def add_el(self, e):
        par, exc = self.get_data()
        self.elements[par] = exc.split(',')
        self._save()
        self.add_row(par)

    def add_row(self, par):
        second_cheet = ','.join(self.elements[par])
        row = self.create_row(par, second_cheet)
        document['tbl_of_exc'].select('tbody')[0] <= row

    def _save(self):
        storage['exclist'] = json.dumps(self.elements)

    def remove(self, e):
        self.remove_row(e)
        self._save()

    def clear_data(self, e):
        datas = document['tbl_of_exc'].select('tbody')[0]
        self.remove_datas(datas)


class Comb:
    def __init__(self):
        self._parametr = CreatParam().create_elem()
        self._exc = CreateExc().create_elem()
        if self._parametr.elements:
            for param in self._parametr.elements:
                self._parametr.add_row(param)
        if self._exc.elements:
            for exc in self._exc.elements:
                self._exc.add_row(exc)

    @property
    def parametr(self):
        return self._parametr

    @property
    def exc(self):
        return self._exc


@bind(document['generate'], 'click')
def generate(e):
    url = 'http://127.0.0.1:5000/generate'
    data = {'parlist': json.loads(storage['parlist']), 'exclist': json.loads(storage['exclist'])}
    ajax.post(url, data=json.dumps(data), oncomplete=output_data)


def output_data(req):
    if document.select('#data_on_page'):
        document['xls_link'].clear()
    if document.select('#rt1'):
        document['output_txt'].clear()
    global _name
    _name = req.text
    link_xls = html.P(html.IMG(loading='lazy', src='/static/img/xlsx_logo.png', width='45px', height='49px', Class='mr-2')+html.A('Скачать данные в формате xlsx', href=f'/static/combs/{_name}.xlsx'))
    link_txt = html.P(html.IMG(loading='lazy', src='/static/img/txt_logo.png', width='45px', height='49px', Class='mr-2')+html.A('Скачать данные в формате txt', href=f'/static/combs/{_name}.txt'))
    document['xls_link'] <= link_xls
    document['xls_link'] <= link_txt
    document['xls_link'] <= html.P(html.IMG(loading='lazy', src='/static/img/arrow_b.png', width='45px', height='49px', Class='mr-2')+ html.A('Вывести данные на странице ниже', id='data_on_page', href='#output-txt'))
    document["data_on_page"].bind('click', output_txt_data)


def output_txt_data(e):
    if not document.select('#rt1'):
        link_txt = f'static/combs/{_name}.txt'
        def read(f):
            document['rt1'].value = f.read()
        div = html.DIV(html.P(),Class='form-group')
        div <= html.TEXTAREA(id = "rt1", rows = "20", cols = "30", autocomplete = "off", Class='form-control')
        document['output_txt'] <= div
        ajax.get(link_txt, oncomplete=read)

try:
    storage['parlist']
    storage['exclist']
except:
    storage['parlist'] = json.dumps({})
    storage['exclist'] = json.dumps({})

page = Comb()
add_parametr = getattr(page.parametr, 'add_el')
add_exc = getattr(page.exc, 'add_el')
clear_data = getattr(page.parametr, 'clear_data')
clear_exc = getattr(page.exc, 'clear_data')

document["add_parametr"].bind("click", add_parametr)
document["add_exc"].bind('click', add_exc)
document["clear_all_par"].bind("click", clear_data)
document["clear_all_exc"].bind('click', clear_exc)