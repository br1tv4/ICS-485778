from prettytable import PrettyTable
from data import dt

x = PrettyTable()

x.field_names = ['Підприємство', 'Площа торг.залу', 'Період', 'Розд.товарообіг', 'Валовий дохід',
                'Витрати обігу', 'Бал.прибуток', 'Чист.прибуток']

for i in range (0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def opentabble():
    print('\nАНАЛІЗ ЗМІНИ ЦІН')
    print(x)