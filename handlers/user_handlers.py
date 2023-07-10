from copy import deepcopy
import requests
from config_data.config import Config, load_config
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, URLInputFile, InputMediaPhoto
from database.database import user_dict_template, users_db
from keyboards.pagination_kb import (create_pag_kb_sd, create_pag_kb_md, create_pag_kb_cd,
                                     create_pag_kb_ssr, create_pag_kb_msr, create_pag_kb_csr,
                                     create_pag_kb_ind, create_pag_kb_skin, create_pag_kb_tin)
from keyboards.other_kb import (create_menu_kb, create_basket_kb_2, create_zero_basket_kb,
                                create_shampoo_kb, create_mask_kb, create_conditioner_kb)
from lexicon.lexicon import (LEXICON, LEXICON_SD_NAME, LEXICON_SD_PHOTO, LEXICON_SD_PRICE,
                             LEXICON_MD_NAME, LEXICON_MD_PHOTO, LEXICON_MD_PRICE,
                             LEXICON_CD_NAME, LEXICON_CD_PHOTO, LEXICON_CD_PRICE,
                             LEXICON_SSR_NAME, LEXICON_SSR_PHOTO, LEXICON_SSR_PRICE,
                             LEXICON_MSR_NAME, LEXICON_MSR_PHOTO, LEXICON_MSR_PRICE,
                             LEXICON_CSR_NAME, LEXICON_CSR_PHOTO, LEXICON_CSR_PRICE,
                             LEXICON_IND_NAME, LEXICON_IND_PHOTO, LEXICON_IND_PRICE,
                             LEXICON_SKIN_NAME, LEXICON_SKIN_PHOTO, LEXICON_SKIN_PRICE,
                             LEXICON_TIN_NAME, LEXICON_TIN_PHOTO, LEXICON_TIN_PRICE)

router: Router = Router()


# загружаем конфиг в переменную config
config: Config = load_config()


# этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_cammand(message: Message):
    if message.from_user.id not in users_db:
        users_db[int(message.from_user.id)] = deepcopy(
            user_dict_template)
        print(users_db)
    text = LEXICON['/start']
    photo = URLInputFile(url=LEXICON['menu_photo'])
    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_menu_kb())


# этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Вернуться в меню"
# во время взаимодействия пользователя с один из каталогов с товарами
@router.callback_query(Text(text='backword_menu'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['/start']
    photo = URLInputFile(url=LEXICON['menu_photo'])
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_menu_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Обновить меню"
# во время взаимодействия пользователя с один из каталогов с товарами
@router.callback_query(Text(text='update'))
async def process_backward_press(callback: CallbackQuery):
    users_db[int(callback.from_user.id)] = deepcopy(
            user_dict_template)
    print(users_db)
    text = LEXICON['/start']
    photo = URLInputFile(url=LEXICON['menu_photo'])
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_menu_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Шампуни"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='shampoo'))
async def process_shampoo_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Выбери производителя😊',
        reply_markup=create_shampoo_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Маски"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='mask'))
async def process_mask_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Выбери производителя😊',
        reply_markup=create_mask_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Кондиционеры"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='cond'))
async def process_conditioner_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Выбери производителя😊',
        reply_markup=create_conditioner_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Шампуни Davines"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='shampoo_d'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_SD_NAME[str(users_db[callback.from_user.id]['sd'])]
    photo = URLInputFile(url=LEXICON_SD_PHOTO[str(
        users_db[callback.from_user.id]['sd'])])
    text_but = f'Купить | {LEXICON_SD_PRICE[str(users_db[callback.from_user.id]["sd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["sd"])}/{len(LEXICON_SD_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_sd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком шампуней Davines
@router.callback_query(Text(text='forward_sd'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['sd'] < len(LEXICON_SD_NAME):
        users_db[callback.from_user.id]['sd'] += 1
    elif users_db[callback.from_user.id]['sd'] == len(LEXICON_SD_NAME):
        users_db[callback.from_user.id]['sd'] = 1
    text = LEXICON_SD_NAME[str(users_db[callback.from_user.id]['sd'])]
    photo = URLInputFile(url=LEXICON_SD_PHOTO[str(
        users_db[callback.from_user.id]['sd'])])
    text_but = f'Купить | {LEXICON_SD_PRICE[str(users_db[callback.from_user.id]["sd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["sd"])}/{len(LEXICON_SD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_sd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком шампуней Davines
@router.callback_query(Text(text='backward_sd'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['sd'] > 1:
        users_db[callback.from_user.id]['sd'] -= 1
    elif users_db[callback.from_user.id]['sd'] == 1:
        users_db[callback.from_user.id]['sd'] = len(LEXICON_SD_NAME)
    text = LEXICON_SD_NAME[str(users_db[callback.from_user.id]['sd'])]
    photo = URLInputFile(url=LEXICON_SD_PHOTO[str(
        users_db[callback.from_user.id]['sd'])])
    text_but = f'Купить | {LEXICON_SD_PRICE[str(users_db[callback.from_user.id]["sd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["sd"])}/{len(LEXICON_SD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_sd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Маски Davines"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='mask_d'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_MD_NAME[str(users_db[callback.from_user.id]['md'])]
    photo = URLInputFile(url=LEXICON_MD_PHOTO[str(
        users_db[callback.from_user.id]['md'])])
    text_but = f'Купить | {LEXICON_MD_PRICE[str(users_db[callback.from_user.id]["md"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["md"])}/{len(LEXICON_MD_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_md(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком масок Davines
@router.callback_query(Text(text='forward_md'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['md'] < len(LEXICON_MD_NAME):
        users_db[callback.from_user.id]['md'] += 1
    elif users_db[callback.from_user.id]['md'] == len(LEXICON_MD_NAME):
        users_db[callback.from_user.id]['md'] = 1
    text = LEXICON_MD_NAME[str(users_db[callback.from_user.id]['md'])]
    photo = URLInputFile(url=LEXICON_MD_PHOTO[str(
        users_db[callback.from_user.id]['md'])])
    text_but = f'Купить | {LEXICON_MD_PRICE[str(users_db[callback.from_user.id]["md"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["md"])}/{len(LEXICON_MD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_md(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком масок Davines
@router.callback_query(Text(text='backward_md'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['md'] > 1:
        users_db[callback.from_user.id]['md'] -= 1
    elif users_db[callback.from_user.id]['md'] == 1:
        users_db[callback.from_user.id]['md'] = len(LEXICON_MD_NAME)
    text = LEXICON_MD_NAME[str(users_db[callback.from_user.id]['md'])]
    photo = URLInputFile(url=LEXICON_MD_PHOTO[str(
        users_db[callback.from_user.id]['md'])])
    text_but = f'Купить | {LEXICON_MD_PRICE[str(users_db[callback.from_user.id]["md"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["md"])}/{len(LEXICON_MD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_md(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Кондиционеры Davines"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='cond_d'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_CD_NAME[str(users_db[callback.from_user.id]['cd'])]
    photo = URLInputFile(url=LEXICON_CD_PHOTO[str(
        users_db[callback.from_user.id]['cd'])])
    text_but = f'Купить | {LEXICON_CD_PRICE[str(users_db[callback.from_user.id]["cd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["cd"])}/{len(LEXICON_CD_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_cd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком кондиционерев Davines
@router.callback_query(Text(text='forward_cd'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['cd'] < len(LEXICON_CD_NAME):
        users_db[callback.from_user.id]['cd'] += 1
    elif users_db[callback.from_user.id]['cd'] == len(LEXICON_CD_NAME):
        users_db[callback.from_user.id]['cd'] = 1
    text = LEXICON_CD_NAME[str(users_db[callback.from_user.id]['cd'])]
    photo = URLInputFile(url=LEXICON_CD_PHOTO[str(
        users_db[callback.from_user.id]['cd'])])
    text_but = f'Купить | {LEXICON_CD_PRICE[str(users_db[callback.from_user.id]["cd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["cd"])}/{len(LEXICON_CD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_cd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком кондиционерев Davines
@router.callback_query(Text(text='backward_cd'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['cd'] > 1:
        users_db[callback.from_user.id]['cd'] -= 1
    elif users_db[callback.from_user.id]['cd'] == 1:
        users_db[callback.from_user.id]['cd'] = len(LEXICON_CD_NAME)
    text = LEXICON_CD_NAME[str(users_db[callback.from_user.id]['cd'])]
    photo = URLInputFile(url=LEXICON_CD_PHOTO[str(
        users_db[callback.from_user.id]['cd'])])
    text_but = f'Купить | {LEXICON_CD_PRICE[str(users_db[callback.from_user.id]["cd"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["cd"])}/{len(LEXICON_CD_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_cd(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Шампуни Dr. Sorbi"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='shampoo_sr'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_SSR_NAME[str(users_db[callback.from_user.id]['ssr'])]
    photo = URLInputFile(url=LEXICON_SSR_PHOTO[str(
        users_db[callback.from_user.id]['ssr'])])
    text_but = f'Купить | {LEXICON_SSR_PRICE[str(users_db[callback.from_user.id]["ssr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ssr"])}/{len(LEXICON_SSR_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_ssr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком шампуней Dr. Sorbi
@router.callback_query(Text(text='forward_ssr'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['ssr'] < len(LEXICON_SSR_NAME):
        users_db[callback.from_user.id]['ssr'] += 1
    elif users_db[callback.from_user.id]['ssr'] == len(LEXICON_SSR_NAME):
        users_db[callback.from_user.id]['ssr'] = 1
    text = LEXICON_SSR_NAME[str(users_db[callback.from_user.id]['ssr'])]
    photo = URLInputFile(url=LEXICON_SSR_PHOTO[str(
        users_db[callback.from_user.id]['ssr'])])
    text_but = f'Купить | {LEXICON_SSR_PRICE[str(users_db[callback.from_user.id]["ssr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ssr"])}/{len(LEXICON_SSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_ssr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком шампуней Dr. Sorbi
@router.callback_query(Text(text='backward_ssr'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['ssr'] > 1:
        users_db[callback.from_user.id]['ssr'] -= 1
    elif users_db[callback.from_user.id]['ssr'] == 1:
        users_db[callback.from_user.id]['ssr'] = len(LEXICON_SSR_NAME)
    text = LEXICON_SSR_NAME[str(users_db[callback.from_user.id]['ssr'])]
    photo = URLInputFile(url=LEXICON_SSR_PHOTO[str(
        users_db[callback.from_user.id]['ssr'])])
    text_but = f'Купить | {LEXICON_SSR_PRICE[str(users_db[callback.from_user.id]["ssr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ssr"])}/{len(LEXICON_SSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_ssr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Маски Dr. Sorbi"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='mask_sr'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_MSR_NAME[str(users_db[callback.from_user.id]['msr'])]
    photo = URLInputFile(url=LEXICON_MSR_PHOTO[str(
        users_db[callback.from_user.id]['msr'])])
    text_but = f'Купить | {LEXICON_MSR_PRICE[str(users_db[callback.from_user.id]["msr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["msr"])}/{len(LEXICON_MSR_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_msr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком масок Dr. Sorbi
@router.callback_query(Text(text='forward_msr'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['msr'] < len(LEXICON_MSR_NAME):
        users_db[callback.from_user.id]['msr'] += 1
    elif users_db[callback.from_user.id]['msr'] == len(LEXICON_MSR_NAME):
        users_db[callback.from_user.id]['msr'] = 1
    text = LEXICON_MSR_NAME[str(users_db[callback.from_user.id]['msr'])]
    photo = URLInputFile(url=LEXICON_MSR_PHOTO[str(
        users_db[callback.from_user.id]['msr'])])
    text_but = f'Купить | {LEXICON_MSR_PRICE[str(users_db[callback.from_user.id]["msr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["msr"])}/{len(LEXICON_MSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_msr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком масок Dr. Sorbi
@router.callback_query(Text(text='backward_msr'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['msr'] > 1:
        users_db[callback.from_user.id]['msr'] -= 1
    elif users_db[callback.from_user.id]['msr'] == 1:
        users_db[callback.from_user.id]['msr'] = len(LEXICON_MSR_NAME)
    text = LEXICON_MSR_NAME[str(users_db[callback.from_user.id]['msr'])]
    photo = URLInputFile(url=LEXICON_MSR_PHOTO[str(
        users_db[callback.from_user.id]['msr'])])
    text_but = f'Купить | {LEXICON_MSR_PRICE[str(users_db[callback.from_user.id]["msr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["msr"])}/{len(LEXICON_MSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_msr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Кондиционеры Dr. Sorbi"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='cond_sr'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_CSR_NAME[str(users_db[callback.from_user.id]['csr'])]
    photo = URLInputFile(url=LEXICON_CSR_PHOTO[str(
        users_db[callback.from_user.id]['csr'])])
    text_but = f'Купить | {LEXICON_CSR_PRICE[str(users_db[callback.from_user.id]["csr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["csr"])}/{len(LEXICON_CSR_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_csr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком кондиционерев Dr. Sorbi
@router.callback_query(Text(text='forward_csr'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['csr'] < len(LEXICON_CSR_NAME):
        users_db[callback.from_user.id]['csr'] += 1
    elif users_db[callback.from_user.id]['csr'] == len(LEXICON_CSR_NAME):
        users_db[callback.from_user.id]['csr'] = 1
    text = LEXICON_CSR_NAME[str(users_db[callback.from_user.id]['csr'])]
    photo = URLInputFile(url=LEXICON_CSR_PHOTO[str(
        users_db[callback.from_user.id]['csr'])])
    text_but = f'Купить | {LEXICON_CSR_PRICE[str(users_db[callback.from_user.id]["csr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["csr"])}/{len(LEXICON_CSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_csr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком кондиционерев Dr. Sorbi
@router.callback_query(Text(text='backward_csr'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['csr'] > 1:
        users_db[callback.from_user.id]['csr'] -= 1
    elif users_db[callback.from_user.id]['csr'] == 1:
        users_db[callback.from_user.id]['csr'] = len(LEXICON_CSR_NAME)
    text = LEXICON_CSR_NAME[str(users_db[callback.from_user.id]['csr'])]
    photo = URLInputFile(url=LEXICON_CSR_PHOTO[str(
        users_db[callback.from_user.id]['csr'])])
    text_but = f'Купить | {LEXICON_CSR_PRICE[str(users_db[callback.from_user.id]["csr"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["csr"])}/{len(LEXICON_CSR_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_csr(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Несмываемые средства"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='indelible'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_IND_NAME[str(users_db[callback.from_user.id]['ind'])]
    photo = URLInputFile(url=LEXICON_IND_PHOTO[str(
        users_db[callback.from_user.id]['ind'])])
    text_but = f'Купить | {LEXICON_IND_PRICE[str(users_db[callback.from_user.id]["ind"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ind"])}/{len(LEXICON_IND_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_ind(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком несмывашек
@router.callback_query(Text(text='forward_ind'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['ind'] < len(LEXICON_IND_NAME):
        users_db[callback.from_user.id]['ind'] += 1
    elif users_db[callback.from_user.id]['ind'] == len(LEXICON_IND_NAME):
        users_db[callback.from_user.id]['ind'] = 1
    text = LEXICON_IND_NAME[str(users_db[callback.from_user.id]['ind'])]
    photo = URLInputFile(url=LEXICON_IND_PHOTO[str(
        users_db[callback.from_user.id]['ind'])])
    text_but = f'Купить | {LEXICON_IND_PRICE[str(users_db[callback.from_user.id]["ind"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ind"])}/{len(LEXICON_IND_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_ind(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком несмывашек
@router.callback_query(Text(text='backward_ind'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['ind'] > 1:
        users_db[callback.from_user.id]['ind'] -= 1
    elif users_db[callback.from_user.id]['ind'] == 1:
        users_db[callback.from_user.id]['ind'] = len(LEXICON_IND_NAME)
    text = LEXICON_IND_NAME[str(users_db[callback.from_user.id]['ind'])]
    photo = URLInputFile(url=LEXICON_IND_PHOTO[str(
        users_db[callback.from_user.id]['ind'])])
    text_but = f'Купить | {LEXICON_IND_PRICE[str(users_db[callback.from_user.id]["ind"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["ind"])}/{len(LEXICON_IND_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_ind(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Уход за кожей головы"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='skin'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_SKIN_NAME[str(users_db[callback.from_user.id]['skin'])]
    photo = URLInputFile(url=LEXICON_SKIN_PHOTO[str(
        users_db[callback.from_user.id]['skin'])])
    text_but = f'Купить | {LEXICON_SKIN_PRICE[str(users_db[callback.from_user.id]["skin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["skin"])}/{len(LEXICON_SKIN_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_skin(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком ухода за кожей головы
@router.callback_query(Text(text='forward_skin'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['skin'] < len(LEXICON_SKIN_NAME):
        users_db[callback.from_user.id]['skin'] += 1
    elif users_db[callback.from_user.id]['skin'] == len(LEXICON_SKIN_NAME):
        users_db[callback.from_user.id]['skin'] = 1
    text = LEXICON_SKIN_NAME[str(users_db[callback.from_user.id]['skin'])]
    photo = URLInputFile(url=LEXICON_SKIN_PHOTO[str(
        users_db[callback.from_user.id]['skin'])])
    text_but = f'Купить | {LEXICON_SKIN_PRICE[str(users_db[callback.from_user.id]["skin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["skin"])}/{len(LEXICON_SKIN_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_skin(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком ухода за кожей головы
@router.callback_query(Text(text='backward_skin'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['skin'] > 1:
        users_db[callback.from_user.id]['skin'] -= 1
    elif users_db[callback.from_user.id]['skin'] == 1:
        users_db[callback.from_user.id]['skin'] = len(LEXICON_SKIN_NAME)
    text = LEXICON_SKIN_NAME[str(users_db[callback.from_user.id]['skin'])]
    photo = URLInputFile(url=LEXICON_SKIN_PHOTO[str(
        users_db[callback.from_user.id]['skin'])])
    text_but = f'Купить | {LEXICON_SKIN_PRICE[str(users_db[callback.from_user.id]["skin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["skin"])}/{len(LEXICON_SKIN_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_skin(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Оттеночные средства"
# во время взаимодействия пользователя со стартовым меню
@router.callback_query(Text(text='tinted'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON_TIN_NAME[str(users_db[callback.from_user.id]['tin'])]
    photo = URLInputFile(url=LEXICON_TIN_PHOTO[str(
        users_db[callback.from_user.id]['tin'])])
    text_but = f'Купить | {LEXICON_TIN_PRICE[str(users_db[callback.from_user.id]["tin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["tin"])}/{len(LEXICON_TIN_NAME)}'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_pag_kb_tin(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком оттеточных средств
@router.callback_query(Text(text='forward_tin'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['tin'] < len(LEXICON_TIN_NAME):
        users_db[callback.from_user.id]['tin'] += 1
    elif users_db[callback.from_user.id]['tin'] == len(LEXICON_TIN_NAME):
        users_db[callback.from_user.id]['tin'] = 1
    text = LEXICON_TIN_NAME[str(users_db[callback.from_user.id]['tin'])]
    photo = URLInputFile(url=LEXICON_TIN_PHOTO[str(
        users_db[callback.from_user.id]['tin'])])
    text_but = f'Купить | {LEXICON_TIN_PRICE[str(users_db[callback.from_user.id]["tin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["tin"])}/{len(LEXICON_TIN_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_tin(pag=pag, text_but=text_but))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком оттеточных средств
@router.callback_query(Text(text='backward_tin'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['tin'] > 1:
        users_db[callback.from_user.id]['tin'] -= 1
    elif users_db[callback.from_user.id]['tin'] == 1:
        users_db[callback.from_user.id]['tin'] = len(LEXICON_TIN_NAME)
    text = LEXICON_TIN_NAME[str(users_db[callback.from_user.id]['tin'])]
    photo = URLInputFile(url=LEXICON_TIN_PHOTO[str(
        users_db[callback.from_user.id]['tin'])])
    text_but = f'Купить | {LEXICON_TIN_PRICE[str(users_db[callback.from_user.id]["tin"])]}₽'
    pag = f'{str(users_db[callback.from_user.id]["tin"])}/{len(LEXICON_TIN_NAME)}'
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=text),
        reply_markup=create_pag_kb_tin(pag=pag, text_but=text_but))


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Корзина"
# # в меню и отправлять пользователю список товаров,
# # добавленных в корзину или сообщение что товаров в корзине нет
# @router.callback_query(Text(text='basket'))
# async def process_basket_press(callback: CallbackQuery):
#     if users_db[callback.from_user.id]['basket']:
#         await callback.message.answer(
#             text='Корзина',
#             reply_markup=create_baskets_kb(
#                 *users_db[callback.from_user.id]['basket']))
#     else:
#         await callback.message.answer(text=LEXICON['no_basket'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Корзина"
# в меню и отправлять пользователю список товаров,
# добавленных в корзину или сообщение что товаров в корзине нет
@router.callback_query(Text(text='basket'))
async def process_basket_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['basket']:
        text = f'\n\n'.join(users_db[callback.from_user.id]['basket'])
        total_sum = 0
        for price in users_db[callback.from_user.id]['basket']:
            total_sum += int(price.split('-')[1].strip().replace('₽', ''))
        await callback.message.delete()
        await callback.message.answer(
            text=text,
            reply_markup=create_basket_kb_2(total_sum))
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=LEXICON['no_basket'],
            reply_markup=create_zero_basket_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# со стоимостью товара и добавлять его в корзину
@router.callback_query(Text(text='price'))
async def process_price_press(callback: CallbackQuery):
    price = callback.message.reply_markup.inline_keyboard[0][0].text.split('|')[
        1].strip()
    name = callback.message.caption.split('.')[0]
    users_db[callback.from_user.id]['basket'].append(
        f'{name}. - {price}')
    print(users_db[callback.from_user.id]['basket'])
    # print(callback.json(indent=4, exclude_none=True))
    await callback.answer('Товар добавлен в корзину!')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# оформления заказа и отправлять сообщение с уведомлением об
# отправке заказа
@router.callback_query(Text(text='sum'))
async def process_sum_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=f'Вы оформили '
        f'заказ на сумму - {callback.message.reply_markup.inline_keyboard[0][0].text.split(":")[1].strip()}.\n\n'
        f'Состав заказа:\n\n{callback.message.text}')
    await callback.message.answer(
        text=LEXICON['order'],
        reply_markup=create_zero_basket_kb())
    params: dict[str, str] = {
        'chat_id': f'{config.tg_bot.admin_ids[0]}',
        'text': f'{callback.from_user.full_name} оформил(а) '
        f'заказ на сумму - {callback.message.reply_markup.inline_keyboard[0][0].text.split(":")[1].strip()}:\n'
        f'tg: {callback.from_user.url}\n\n'
        f'Состав заказа:\n\n{callback.message.text}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
    users_db[callback.from_user.id]['basket'].clear()


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Редактировать"
# # и отправлять клавиатуры с товарами добалеными в корзину для редактирования
# @router.callback_query(Text(text='edit'))
# async def process_edit_press(callback: CallbackQuery):
#     await callback.message.delete()
#     for num in users_db[callback.from_user.id]['basket']:
#         await callback.message.answer(text=num,
#                                       reply_markup=create_zero_basket_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Очистить корзину"
# и отправлять сообщение об очистке корзины
@router.callback_query(Text(text='clear'))
async def process_clear_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['basket'].clear()
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['no_basket'],
        reply_markup=create_zero_basket_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки пагинации
# во время взаимодействия пользователя со списком товаров
@router.callback_query(Text(text='pag'))
async def process_pag_press(callback: CallbackQuery):
    await callback.answer()