# Порядок ввода: tuple(краткое имя, русское вариант) ......
# Перевод на англ, автоматический
class TextMessage:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *args):
        self.__text = self.__args_to_dict(args)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        raise ValueError('You can not change this attribute')

    @classmethod
    def __args_to_dict(cls, arguments: tuple):
        res = {'ru': {},
               'en': {}}

        for i in arguments:
            for index, value in enumerate(i):
                if index % 3 == 1:
                    res['ru'][i[0]] = value
                elif index % 3 == 2:
                    res['en'][i[0]] = value
                else:
                    continue
        return res

    def __call__(self, short_name_text_mes: str, lang: str):
        return self.__text[lang][short_name_text_mes]


TEXT = TextMessage(('welcome', 'Добро пожаловать, ', 'Welcome, '),
                   ('hello', '✅ Пройди регистрацию в пару кликов', '✅ Register in a couple of clicks:'),
                   ('choose_role', 'Выбери роль', 'Choose your role'),
                   ('choose_sub_info_group', 'Выбери класс', 'Choose your class'),
                   ('choose_sub_info_teacher', 'Выбери ФИО', "Choose the teacher's full name"),
                   ('choose_sub_info_auditory', 'Выбери аудиторию', 'Choose auditory'),
                   ('student', '👨‍🎓Ученик', '👨‍🎓Student'),
                   ('teacher', '👨‍🏫Преподаватель', '👨‍🏫Teacher'),
                   ('parent', '👨‍👩‍👧Родитель', '👨‍👩‍👧Parent'),
                   ('teacher_kb', 'Для преподавателя', 'For a teacher'),
                   ('auditory', 'Для аудитории', 'For an auditory'),
                   ('group', 'Для класса', 'For a group'),
                   ('registration_done', '✅ Регистрация прошла успешно', '✅ Registration was successful'),
                   ('today', 'На сегодня', 'For today'),
                   ('tomorrow', 'На завтра', 'For tomorrow'),
                   ('all', 'Все расписание', 'All schedule'),
                   ('main', 'Показать расписание', 'Show the schedule'),  # ЗАМЕТЬТЕ РАЗНИЦУ
                   ('main_schedule', 'Расписание на', 'Schedule for'),
                   ('month', ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                              'Октябрь', 'Ноябрь', 'Декабрь'],
                    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']),
                   ('weekdays', {
                       1: 'Понедельник',
                       2: 'Вторник',
                       3: 'Среду',
                       4: 'Четверг',
                       5: 'Пятницу',
                       6: 'Субботу',
                       7: 'Воскресенье'
                   },
                    {
                        1: 'Monday',
                        2: 'Tuesday',
                        3: 'Wednesday',
                        4: 'Thursday',
                        5: 'Friday',
                        6: 'Saturday',
                        7: 'Sunday'
                    }),
                   ('weekdays_kb', {
                       1: 'Понедельник',
                       2: 'Вторник',
                       3: 'Среда',
                       4: 'Четверг',
                       5: 'Пятница',
                       6: 'Суббота',
                       7: 'Воскресенье'
                   },
                    {
                        1: 'Monday',
                        2: 'Tuesday',
                        3: 'Wednesday',
                        4: 'Thursday',
                        5: 'Friday',
                        6: 'Saturday',
                        7: 'Sunday'
                    }),
                   ('choose_type', 'Для кого/чего ищешь расписание?',
                    'Who/what are you looking for a schedule for?'),
                   ('choose_day', 'Выбери день недели', 'Choose a day of the week'),
                   ('no_schedule', '❎ Занятий нет', '❎ There are no classes'),
                   ('all_days', 'На конкретный день недели', 'For a specific day of the week'),
                   ('choose_letter', 'Выбери первую букву фамилии',
                    "Choose the first letter of last name"),
                   ('back', '⬅ Назад', '⬅ Back'),
                   ('changed_schedule', 'Изменения в расписании на', 'Schedule changes for'),
                   ('yes', 'Да', 'Yes'),
                   ('no', 'Нет', 'No'),
                   ('aus', "Вы уверены?", 'Are you sure?'),
                   ('admin_sending_message', 'Сообщения отправлены, ошибок - ', 'Messages sent, errors - '),
                   ('get_feedback', 'Дорогой друг! Если тебе понравился этот бот или у тебя есть предложение, '
                                    'как сделать его еще лучше - напиши и отправь нам сообщение в этот чат',
                    'Dear friend! If you liked this bot, or you have suggestions on how to make it even better, '
                    'write and send us a message to this chat'),
                   ('feedback_done', 'Отзыв успешно отправлен. Благодарим за обратную связь 🤝',
                    'The review has been sent successfully. Thanks for the feedback. 🤝'),
                   ('administration_role', 'Администрация', 'Administration'),
                   ('optional_func', 'Дополнительные функции', 'Optional functions'),
                   ('choose_optional_function', 'Выбери дополнительную функцию', 'Select additional function'),
                   ('free_auditory', 'Свободные аудитории', 'Free audiences'),
                   ('official_site', 'Официальный сайт расписания СУНЦ УрФУ',
                    'Official website of the schedule of the SESC of UrFU'),
                   ('choose_lesson', 'Выбери урок', 'Choose a lesson'),
                   ('lesson', 'Урок', 'Lesson'),
                   ('today_btn', 'Сегодня', 'Today'),
                   ('bell_schedule', 'Расписание звонков', 'Bell schedule'),
                   ('administration_role', 'Администратор', 'Administrator'),
                   ('send_your_pass', 'Отправьте фото вашего пропуска', "Send a photo of your pass"),
                   ('confirmation', 'Запрос отправлен на рассмотрение. Если хочешь, то можешь зарегистрироваться на '
                                    'не административную роль. Мы пришлем тебе уведомление о том что твоя заявка '
                                    'принята или отклонена',
                    'The request has been sent for consideration. If you want, you can sign up for a '
                    'non-administrative role. We will send you a notification that your application has been accepted '
                    'or rejected.'),
                   ("administrator_dismissed", 'Ваша заявка была отклонена', 'Your application has been rejected'),
                   ("new_administrator_text", 'Ваша заявка была одобрена', 'Your application has been approved'),
                   ('admin_panel', 'Функции: ', 'Functions: '),
                   ("change_schedule", "Изменить расписание", "Change schedule"))