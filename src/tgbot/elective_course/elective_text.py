from enum import Enum


class ElectiveText(Enum):
    add = {'ru': 'Добавить факультатив',
           'en': 'Add an elective'}
    remove = {'ru': 'Удалить факультатив',
              'en': 'Remove optional'}
    to_main = {'ru': 'На главную',
               'en': 'To main'}
    main_page = {'ru': 'Факультативы',
                 'en': 'Elective courses'}
    register_to_new_course = {'ru': 'Зарегистрироваться на новый факультатив',
                              'en': 'Register for a new elective'}
    choose_pulpit = {'ru': 'Выберите кафедру',
                     'en': 'Choose a pulpit'}

    choose_elective = {'ru': 'Выберите факультатив',
                       'en': 'Choose an elective'}
