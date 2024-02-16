from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from tgbot.parser import PARSER
from models.db import DB
from models.database import get_async_session
import datetime
from tgbot.sesc_info import SESC_Info

from tgbot.text import TEXT
from tgbot.keyboard import get_choose_schedule, get_choose_weekday_kb

from tgbot.handlers.auxiliary import send_schedule

router = Router()


@router.callback_query(F.data == 'today')
async def send_schedule_for_today(callback: CallbackQuery):
    session = await get_async_session()
    user_data = await DB().select_user_by_id(session, callback.message.chat.id)
    lang = callback.from_user.language_code

    await callback.message.delete()

    day = str((datetime.date.today().weekday()) % 6 + 1)
    file = await PARSER.parse(user_data['role'], user_data['sub_info'], day)

    # проверка на присутствие расписания
    if file == 'NO_SCHEDULE':
        await callback.message.answer(TEXT('no_schedule', lang),
                                      disable_notification=True)
    else:
        schedule = FSInputFile(file)
        await send_schedule(chat_id=callback.message.chat.id,
                            lang=lang,
                            role=user_data['role'],
                            sub_info=user_data['sub_info'],
                            schedule=schedule,
                            short_name_text_mes='main',
                            weekday=int(day))

    await callback.message.answer(TEXT('main', lang),
                                  reply_markup=get_choose_schedule(lang),
                                  disable_notification=True)
    await callback.answer()


@router.callback_query(F.data == 'tomorrow')
async def send_schedule_for_tomorrow(callback: CallbackQuery):
    session = await get_async_session()
    user_data = await DB().select_user_by_id(session, callback.message.chat.id)
    lang = callback.from_user.language_code

    await callback.message.delete()
    today_to_tomorrow = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '1'}
    day = today_to_tomorrow[datetime.date.today().weekday()]

    file = await PARSER.parse(user_data['role'], user_data['sub_info'], day)

    # проверка на присутствие расписания
    if file == 'NO_SCHEDULE':
        await callback.message.answer(TEXT('no_schedule', lang),
                                      disable_notification=True)
    else:
        schedule = FSInputFile(file)
        await send_schedule(chat_id=callback.message.chat.id,
                            lang=lang,
                            role=user_data['role'],
                            sub_info=user_data['sub_info'],
                            schedule=schedule,
                            short_name_text_mes='main',
                            weekday=int(day))

    await callback.message.answer(TEXT('main', lang),
                                  reply_markup=get_choose_schedule(lang),
                                  disable_notification=True)
    await callback.answer()


@router.callback_query(F.data == 'all_days')
async def get_all_days_sch(callback: CallbackQuery):
    lang = callback.from_user.language_code

    await callback.message.delete()
    await callback.message.answer(TEXT('choose_day', lang),
                                  reply_markup=get_choose_weekday_kb(lang, back=False),
                                  disable_notification=True)

    await callback.answer()


@router.callback_query(F.data == '1')
@router.callback_query(F.data == '2')
@router.callback_query(F.data == '3')
@router.callback_query(F.data == '4')
@router.callback_query(F.data == '5')
@router.callback_query(F.data == '6')
async def get_sch_for_this_day(callback: CallbackQuery):
    lang = callback.from_user.language_code
    session = await get_async_session()
    user_data = await DB().select_user_by_id(session, callback.message.chat.id)
    file = await PARSER.parse(user_data['role'], user_data['sub_info'], callback.data)

    await callback.message.delete()
    if file == 'NO_SCHEDULE':
        await callback.message.answer(TEXT('no_schedule', lang),
                                      disable_notification=True)
    else:
        schedule = FSInputFile(file)
        await send_schedule(chat_id=callback.message.chat.id,
                            schedule=schedule,
                            short_name_text_mes='main',
                            role=user_data['role'],
                            sub_info=user_data['sub_info'],
                            weekday=int(callback.data),
                            lang=lang)

    await callback.message.answer(TEXT('main', lang),
                                  reply_markup=get_choose_schedule(lang),
                                  disable_notification=True)

    await callback.answer()
