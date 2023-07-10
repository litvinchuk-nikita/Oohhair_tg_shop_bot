from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_menu_kb() -> InlineKeyboardMarkup:
    shampoo_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Шампуни', callback_data='shampoo')
    conditioner_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Кондиционеры', callback_data='cond')
    mask_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Маски', callback_data='mask')
    indelible_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Несмываемый уход', callback_data='indelible')
    skin_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Уход за кожей головы', callback_data='skin')
    tinted_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Оттеночные средства', callback_data='tinted')
    basket_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Корзина', callback_data='basket')
    update_menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Обновить меню', callback_data='update')
    kb_builder_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_menu.add(shampoo_button, mask_button, conditioner_button,
                        indelible_button, skin_button, tinted_button, basket_button,
                        update_menu_button)
    kb_builder_menu.adjust(1, 1, 1, 1, 1, 1, 2)
    return kb_builder_menu.as_markup()


def create_mask_kb() -> InlineKeyboardMarkup:
    mask_davines_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Маски Davines', callback_data='mask_d')
    mask_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Маски Dr. Sorbie', callback_data='mask_sr')
    kb_builder_mask: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_mask.add(mask_davines_button, mask_drsorbi_button)
    kb_builder_mask.adjust(1, 1)
    return kb_builder_mask.as_markup()


def create_shampoo_kb() -> InlineKeyboardMarkup:
    shampoo_davines_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Шампуни Davines', callback_data='shampoo_d')
    shampoo_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Шампуни Dr. Sorbie', callback_data='shampoo_sr')
    kb_builder_shampoo: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_shampoo.add(shampoo_davines_button, shampoo_drsorbi_button)
    kb_builder_shampoo.adjust(1, 1)
    return kb_builder_shampoo.as_markup()


def create_conditioner_kb() -> InlineKeyboardMarkup:
    conditioner_davines_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Кондиционеры Davines', callback_data='cond_d')
    conditioner_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Кондиционеры Dr. Sorbie', callback_data='cond_sr')
    kb_builder_conditioner: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_conditioner.add(conditioner_davines_button, conditioner_drsorbi_button)
    kb_builder_conditioner.adjust(1, 1)
    return kb_builder_conditioner.as_markup()



# def create_baskets_kb(*args: str) -> InlineKeyboardMarkup:
#     # создаем объект клавиатуры
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     # наполняем клавиатуру кнопками-закладками в порядке возрастания
#     for button in args:
#         kb_builder.row(InlineKeyboardButton(
#             text=f'{button}',
#             callback_data=f'{button.split("-")[0].strip()}'))
#     # добавляем в клавиатуру в конце две кнопки "Редактировать и "Отменить"
#     kb_builder.row(InlineKeyboardButton(
#         text='Редактировать',
#         callback_data='edit_basket'),
#         InlineKeyboardButton(
#             text='Вернуться в меню',
#             callback_data='backword_menu'),
#         width=2)
#     return kb_builder.as_markup()


def create_basket_kb(total_sum) -> InlineKeyboardMarkup:
    sum_button: InlineKeyboardButton = InlineKeyboardButton(
        text=f'Оформить заказ: {total_sum}₽', callback_data='sum')
    edit_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Редактировать', callback_data='edit')
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_basket.add(sum_button, edit_button, menu_button)
    kb_builder_basket.adjust(1, 2)
    return kb_builder_basket.as_markup()


def create_zero_basket_kb() -> InlineKeyboardMarkup:
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder_zero_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_zero_basket.add(menu_button)
    return kb_builder_zero_basket.as_markup()


def create_basket_kb_2(total_sum) -> InlineKeyboardMarkup:
    sum_button: InlineKeyboardButton = InlineKeyboardButton(
        text=f'Оформить заказ: {total_sum}₽', callback_data='sum')
    edit_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Очистить корзину', callback_data='clear')
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_basket.add(sum_button, edit_button, menu_button)
    kb_builder_basket.adjust(1, 2)
    return kb_builder_basket.as_markup()
