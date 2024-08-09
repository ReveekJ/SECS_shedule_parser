import datetime

from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.tgbot import feedback, auxiliary, admin
from src.tgbot.auxiliary import bot
from src.tgbot.changes.changes import sending_schedule_changes
from src.tgbot.elective_course import dialogs
from src.tgbot.for_administration import administration_work
from src.tgbot.main_work import allSchedule, relogin, mainPage, registration, optional_menu


def set_tasks(scheduler: AsyncIOScheduler):
    times = [datetime.time(2, 0, 0),
             datetime.time(5, 0, 0),
             datetime.time(6, 0, 0),
             datetime.time(7, 0, 0),
             datetime.time(9, 30, 0),
             datetime.time(10, 20, 0),
             datetime.time(11, 10, 0),
             datetime.time(12, 10, 0),
             datetime.time(13, 5, 0),
             datetime.time(14, 5, 0),
             datetime.time(15, 5, 0),
             datetime.time(18, 0, 0),
             datetime.time(20, 0, 0)]

    for i in times[:len(times) - 1]:
        # минус 2, так как сервер находится в Москве
        scheduler.add_job(sending_schedule_changes, CronTrigger(hour=i.hour - 2, minute=i.minute, second=i.second))

    scheduler.add_job(sending_schedule_changes, CronTrigger(hour=times[-1].hour, minute=times[-1].minute,
                                                            second=times[-1].second),
                      next_run_time=datetime.datetime.now())


dp = Dispatcher()


if __name__ == '__main__':
    # ставим выполняться проверку изменений
    scheduler = AsyncIOScheduler()
    set_tasks(scheduler)
    scheduler.start()

    dp.include_routers(administration_work.router, auxiliary.router, registration.router, allSchedule.router,
                       optional_menu.router, mainPage.router, relogin.router, admin.router, feedback.router,
                       dialogs.admin_work, dialogs.user_work)
    setup_dialogs(dp)
    dp.run_polling(bot)
