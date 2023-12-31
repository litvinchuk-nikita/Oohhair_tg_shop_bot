LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': f'Приятных покупок🛒',
    '/help': f'Привет! 💛 На связи Света OOHHAIR. Этот телеграмм-бот создан для заказа домашнего ухода продукции Dr.Sorbi и Davines.'
             f'Как он работает? Выбирай, что тебе нужно, добавляй в корзину 🗑️ и жми «оформить заказ». После, с тобой свяжутся для уточнения деталей 📦\n\n'
             f'Доступные команды:\n'
             f'/start - Запустить бота/открыть меню\n'
             f'/help - Справка по работе бота',
    'other': f'Не понимаю вас..\nДля ознакомления с возможностями бота введите команду /help',
    'no_basket': 'Товары в корзину не добавлены',
    'order': 'Заказ оформлен, после проверки наличия таваров, я напишу тебе в личные сообщения😊',
    'menu_photo': 'https://sun9-58.userapi.com/impg/OHFUuEzx8hW27QGRiNp-W_AVorN0F1T62-smmw/_gndLoVbfWI.jpg?size=2050x1284&quality=95&sign=22d7f92c14259bd37c27820f349fb943&type=album'}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Запустить бота/открыть меню',
    '/help': 'Справка по работе бота'}

LEXICON_SD_NAME: dict[str, str] = {
    '1': f'Питательный шампунь NOUNOU, 250мл.\n\nОздоравливает и питает сухие и поврежденные волосы.',
    '2': f'Увлажняющий шампунь MOMO, 250мл.\n\nДеликатно очищает сухие и обезвоженные волосы.',
    '3': f'Шампунь для придания объема VOLU, 250мл.\n\nНежно очищает и уплотняет волосы, не перегружая их.',
    '4': f'Шампунь для усиления завитка LOVE, 250мл.\n\nМягко и деликатно очищает вьющиеся волосы и придает им объем, эластичность и мягкость.',
    '5': f'Шампунь для абсолютной красоты OI, 280мл.\n\nДеликатно очищает волосы и придает необычайную мягкость, блеск и объем.',
    '6': f'Активный энергетический шампунь NATURAL TECH ENERGIZING, 250мл.\n\nЭффективно очищает и ухаживает за хрупкими истонченными волосами, склонными к выпадению. Стимулирует микроциркуляцию кожи головы.',
    '7': f'Защитный шампунь MINU, 250мл.\n\nМягко очищает волосы, сохраняя цвет окрашенных волос и придаёт волосам блеск и шелковистость.',
    '8': f'Очищающий шампунь NATURAL TECH PURIFYING, 250мл.\n\nСоздан специально для борьбы с сухой или жирной перхотью.',
    '9': f'Мягко очищающий шампунь NATURAL TECH REPLUMPING, 250мл.\n\nПридает волосам эластичность и активно увлажняет, сохраняя структуру волос здоровой.',
    '10': f'Шампунь для предотвращения ломкости MELU, 250мл.\n\nБережно очищает поврежденные или длинные волосы и придает локонам блеск и упругость.',
    '11': f'Деликатный шампунь DEDE, 250мл.\n\nМягко очищает волосы и подходит для ежедневного применения.',
    '12': f'Питательный шампунь NATURAL TECH NOURISHING, 250мл.\n\nДля сухих и поврежденных волос любого типа.',
    '13': f'Шампунь для сияния блонд HEART OF GLASS, 250мл.\n\nДеликатный шампунь для поддержания различных, в том числе и натуральных оттенков блонд.',
    '14': f'Увлажняющий шампунь NATURAL TECH WELL-BEING, 250мл.\n\nБережно очищает кожу головы и волосы, без эффекта утяжеления.',
    '15': f'Балансирующий шампунь NATURAL TECH REBALANCING, 250мл.\n\nНормализует работу сальных желез и стабилизирует производство кожного сала.',
    '16': f'Смягчающий шампунь LOVE, 250мл.\n\nБережно очищает и разглаживает волнистые волосы.',
    '17': f'Активно освежающий шампунь SOLU, 250мл.\n\nГлубоко очищает волосы и кожу головы, удаляя остатки стайлинговых продуктов.',
    '18': f'Восстанавливающий шампунь-скраб NATURAL TECH DETOXIFYING, 250мл.\n\nДеликатно очищает и скрабирует ослабленную, атоничную кожу головы.',
    '19': f'Деликатный обновляющий шампунь NATURAL TECH RENEWING, 250мл.\n\nБережно очищает волосы и продлевает жизненный цикл волос.',
    '20': f'Шампунь-гель Аутентик с маслянистой текстурой, 280мл.\n\nМягко очищает и увлажняет кожу, делая ее гладкой и шелковистой.',
    '21': f'Успокаивающий шампунь NATURAL TECH CALMING, 250мл.\n\nБережно очищает кожу головы и придает локонам шелковистость и блеск.',
    '22': f'Деликатный восстанавливающий увлажняющий шампунь-гель для волос и тела SU, 250мл.\n\nДля применения после пребывания на солнце. Гарантирует увлажнение и защиту волос и кожи, помогает сохранить загар.',
    '23': f'Деликатный шампунь для волос и тела WE STAND, 250мл.\n\nДелает кожу мягкой, а волосы блестящими и шелковистыми.',
    '24': f'Невидимый сухой шампунь для любого типа волос MORE INSIDE, 250мл.\n\nБережно очищает от корней до кончиков, абсорбирует излишки кожного сала, освежает волосы и придает им приятный аромат.'}


LEXICON_SD_PRICE: dict[str, str] = {
    '1': '2300',
    '2': '2300',
    '3': '2300',
    '4': '2300',
    '5': '3000',
    '6': '2700',
    '7': '2300',
    '8': '2700',
    '9': '2700',
    '10': '2300',
    '11': '2300',
    '12': '2700',
    '13': '2800',
    '14': '2700',
    '15': '2700',
    '16': '2300',
    '17': '2300',
    '18': '2700',
    '19': '2700',
    '20': '2700',
    '21': '2700',
    '22': '2300',
    '23': '2300',
    '24': '3100'}


LEXICON_SD_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nounou-shampun-dlya-uplotneniya-volos.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2019/04/momo-shampun-dlya-uvlazhneniya-volos.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2019/04/volu-shampun-dlya-pridaniya-obema.jpg',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-25-1.jpg',
    '5': 'https://cdn.davines.ru/wp-content/uploads/2019/03/oi-shampun-dlya-absolyutnoj-krasoty-volos.jpg',
    '6': 'https://cdn.davines.ru/wp-content/uploads/2019/04/energeticheskij-shampun.jpg',
    '7': 'https://cdn.davines.ru/wp-content/uploads/2019/04/new-project-41-1.jpg',
    '8': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ochishhayushhij-shampun-protiv-perhoti.jpg',
    '9': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-replumping-uplotnyayushhij-shampun7.jpg',
    '10': 'https://cdn.davines.ru/wp-content/uploads/2019/04/new-project-38.jpg',
    '11': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-20.jpg',
    '12': 'https://cdn.davines.ru/wp-content/uploads/2020/01/nt-nourishing-pitatelnyj-shampun-33.jpg',
    '13': 'https://cdn.davines.ru/wp-content/uploads/2021/04/72000_heartofglass_shampoo_250ml_davines_2000x-1-2.jpg',
    '14': 'https://cdn.davines.ru/wp-content/uploads/2019/04/uvlazhnyayushhij-shampun-dlya-vseh-tipov-volos-2.jpg',
    '15': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-rebalancing-balansiruyushhij-shampun-22.jpg',
    '16': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-21.jpg',
    '17': 'https://cdn.davines.ru/wp-content/uploads/2019/04/solu-osvezhayushhij-shampun-dlya-glubokogo-ochishheniya.jpg',
    '18': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-detoxifying-detoksicziruyushhij-shampun-skrab.jpg',
    '19': 'https://cdn.davines.ru/wp-content/uploads/2019/04/obnovlyayushhij-shampun.jpg',
    '20': 'https://cdn.davines.ru/wp-content/uploads/2019/04/autentik-ochishhayushhij-nektar.jpg',
    '21': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-calming-uspokaivayushhij-shampun.jpg',
    '22': 'https://cdn.davines.ru/wp-content/uploads/2019/04/su-shampun-dlya-volos-i-tela.jpg',
    '23': 'https://cdn.davines.ru/wp-content/uploads/2023/03/2175614_dehc_hairbody-wash_250ml_wsb-3-copy-2.jpg',
    '24': 'https://cdn.davines.ru/wp-content/uploads/2022/07/87113_more_inside_invisible_dry_shampoo_250ml-copy.jpg'}


LEXICON_MD_NAME: dict[str, str] = {
    '1': f'Суперпитательная и супербыстродействующая маска The Renaissance Circle, 50мл.\n\nБережно ухаживает за хрупкими и ломкими волосами, питая и увлажняя каждый локон.',
    '2': f'Маска-суперблеск The Spotlight Circle, 50мл.\n\nСоздана для придания волосам потрясающего блеска, подчеркивает естественный или косметический цвет.',
    '3': f'Питательная маска OI для всех типов волос, 250мл.\n\nБережно смягчает локоны, создавая защитную пленку, без утяжеления.',
    '4': f'Быстродействующая многофункциональная маска для волос The Quick Fix Circle, 50мл.\n\nБережно ухаживает и увлажняет даже самые сухие и непослушные волосы.',
    '5': f'Маска NT NOURISHING HAIR BUILDING PAK, 250мл.\n\nСоздана специально для питания и реструктуризации сухих и поврежденных волос.',
    '6': f'Успокаивающая маска для волос и кожи головы The Wake Up Circle, 50мл.\n\nПридает великолепный объем волосам и тонизирует кожу головы.',
    '7': f'Маска The Restless Circle, 50мл.\n\nПридаёт волосам плотность и эластичность. Экстракт семян чиа в составе маски помогает укрепить кутикулу волос и улучшить их внешний вид.',
    '8': f'Смягчающая увлажняющая маска для волос и кожи головы The Let It Go Circle, 50мл.\n\nПитает волосы и успокаивает кожу головы после стресса.',
    '9': f'Маска-детокс для волос и кожи головы The Purity Circle, 50мл.\n\nБережно ухаживает за волосами, придавая локонам мягкости и шелковистости.',
    '10': f'Глубоко увлажняющая интенсивно питающая маска NT NOURISHING VEGETARIAN MIRACLE, 250мл.\n\nПредназначена для сухих и поврежденных волос.',
    '11': f'Маска Heart of Glass, 150мл.\n\nВосстанавливает повреждённые участки осветлённых волос, защищают их от ломкости, обладают интенсивным питательным эффектом, что придаёт волосам дополнительную силу, блеск и защиту.',
    '12': f'Интенсивная восстанавливающая маска NOUNOU, 250мл.\n\nОздоравливает и питает сухие и поврежденные волосы.',
    '13': f'Маска для окрашенных волос MINU, 250мл.\n\nДеликатно ухаживает, сохраняя цвет и придаёт волосам блеск и шелковистость.',
    '14': f'Маска для усиления завитка LOVE, 250мл.\n\nПридает вьющимся волосам объем, эластичность и мягкость. ',
    '15': f'Мгновенно разглаживающая маска для волнистых и непослушных волос LOVE, 250мл.\n\nДелает волосы гладкими и эластичными, облегчает процесс расчесывания и укладки.'}


LEXICON_MD_PRICE: dict[str, str] = {
    '1': '1000',
    '2': '1000',
    '3': '4450',
    '4': '1000',
    '5': '4300',
    '6': '1000',
    '7': '1000',
    '8': '1000',
    '9': '1000',
    '10': '4100',
    '11': '3000',
    '12': '3300',
    '13': '3300',
    '14': '3300',
    '15': '3300'}


LEXICON_MD_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2019/04/maska-vosstanovlenie-dlya-hrupkih-volos5.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2019/03/maska-superblesk-dlya-volos-the-spotlight-circle23.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2019/07/oi-pitatelnoe-maslo.jpg',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2019/04/mnogofunkczionalnaya-maska-dlya-volos.jpg',
    '5': 'https://cdn.davines.ru/wp-content/uploads/2020/01/hair-building-pak-3.jpg',
    '6': 'https://cdn.davines.ru/wp-content/uploads/2019/04/maska-anti-stress-dlya-volos-i-kozhi-golovy.jpg',
    '7': 'https://cdn.davines.ru/wp-content/uploads/2019/09/maska-superfud-dlya-neugomonnyh-volos-54.jpg',
    '8': 'https://cdn.davines.ru/wp-content/uploads/2019/04/maska-relaks-dlya-volos-i-kozhi-golovy.jpg',
    '9': 'https://cdn.davines.ru/wp-content/uploads/2019/04/maska-detoks-dlya-volos-i-kozhi-golovy36.jpg',
    '10': 'https://cdn.davines.ru/wp-content/uploads/2020/01/nt-nourishing-intensivno-pitayushhaya-maska-“vegetarianskoe-chudo”.jpg',
    '11': 'https://cdn.davines.ru/wp-content/uploads/2021/04/72006_heartofglass_treatment_150ml_davines_2000x-1-1.jpg',
    '12': 'https://cdn.davines.ru/wp-content/uploads/2022/03/nounou-mask-1-1.jpg',
    '13': 'https://cdn.davines.ru/wp-content/uploads/2022/03/minu-mask-1-1.jpg',
    '14': 'https://cdn.davines.ru/wp-content/uploads/2022/06/love-curl-mask-1-1.jpg',
    '15': 'https://cdn.davines.ru/wp-content/uploads/2022/08/love-smoothing.jpg'}


LEXICON_CD_NAME: dict[str, str] = {
    '1': f'Кондиционер для абсолютной красоты волос OI, 250мл.\n\nСодержит масло аннато из растения, произрастающего в лесах Амазонии, а также кондиционирующее вещество, полученное из целлюлозы, придающее мягкость структуре волос.',
    '2': f'Уплотняющий кондиционер NATURAL TECH REPLUMPING, 150мл.\n\nУхаживает и придает волосам эластичность, объем и плотность.',
    '3': f'Увлажняющий и питающий кондиционер NT NOURISHING VEGETARIAN MIRACLE, 250мл.\n\nПредназначен для сухих и поврежденных волос. ',
    '4': f'Увлажняющий кондиционер NATURAL TECH WELL-BEING, 150мл.\n\nБережно ухаживает за волосами, придавая им блеск и шелковистость без утяжеления.',
    '5': f'Увлажняющий кондиционер MOMO, 250мл.\n\nБережно ухаживает за сухими и обезвоженными волосами.',
    '6': f'Интенсивный питательный кондиционер Heart of Glass, 250мл.\n\nСпособствует поддержанию оттенков блонд, а также обладает выраженным увлажняющим, восстанавливающим и кондиционирующим действием.',
    '7': f'Кондиционер для усиления завитка LOVE, 250мл.\n\nПридает вьющимся волосам объем, эластичность и мягкость.',
    '8': f'Питательный кондиционер NOUNOU, 250мл.\n\nОздоравливает и питает сухие и поврежденные волосы.',
    '9': f'Обновляющий кондиционер NATURAL TECH RENEWING, 250мл.\n\nУвлажняет и продлевает жизненный цикл волос. Помогает поддерживать естественную красоту и здоровое состояние кожи головы и волос. Питает, увлажняет и стимулирует кожу головы и волосы. Оставляет волосы здоровыми, плотными и блестящими, не перегружая их.',
    '10': f'Защитный кондиционер MINU, 250мл.\n\nСохраняет цвет окрашенных волос и придаёт им блеск и шелковистость.',
    '11': f'Кондиционер для предотвращения ломкости MELU, 250мл.\n\nПитает поврежденные или длинные волосы и придает локонам блеск и упругость.',
    '12': f'Разглаживающий кондиционер LOVE, 250мл.\n\nПозволяет бережно ухаживать и разглаживать волнистые волосы.',
    '13': f'Деликатный кондиционер DEDE, 250мл.\n\nБережно ухаживает за волосами и подходит для ежедневного применения.'}


LEXICON_CD_PRICE: dict[str, str] = {
    '1': '3500',
    '2': '2700',
    '3': '3300',
    '4': '2700',
    '5': '2550',
    '6': '3500',
    '7': '2550',
    '8': '2550',
    '9': '3300',
    '10': '2550',
    '11': '2550',
    '12': '2550',
    '13': '2550'}


LEXICON_CD_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2019/03/oi-kondiczioner-dlya-absolyutnoj-krasoty-volos.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-replumping-uplotnyayushhij-kondiczioner-4.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2020/01/nt-nourishing-pitatelnyj-kondiczioner-“vegetarianskoe-chudo”.jpg',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2019/04/uvlazhnyayushhij-kondiczioner-dlya-zdorovya-volos.jpg',
    '5': 'https://cdn.davines.ru/wp-content/uploads/2022/01/momo-cond-1-1.jpg',
    '6': 'https://cdn.davines.ru/wp-content/uploads/2021/04/72003_heartoflgass_conditioner_250ml_davines_2000x-1-1.jpg',
    '7': 'https://cdn.davines.ru/wp-content/uploads/2021/12/lovecurl-cond.jpg',
    '8': 'https://cdn.davines.ru/wp-content/uploads/2022/03/nounou-cond-1-1.jpg',
    '9': 'https://cdn.davines.ru/wp-content/uploads/2019/04/obnovlyayushhij-kondiczioniruyushhij-uhod.jpg',
    '10': 'https://cdn.davines.ru/wp-content/uploads/2022/03/minu-cond-1-1.jpg',
    '11': 'https://cdn.davines.ru/wp-content/uploads/2022/03/melu-cond-1-1.jpg',
    '12': 'https://cdn.davines.ru/wp-content/uploads/2022/03/love-sm-1-1.jpg',
    '13': 'https://cdn.davines.ru/wp-content/uploads/2022/03/dede-cond-2.jpg'}


LEXICON_SSR_NAME: dict[str, str] = {
    '1': f'Питательный антивозрастной шампунь TREATMENT, 400мл.\n\nСоздан на основе натуральных ингредиентов специально для сухих, химически обработанных, возрастных и окрашенных волос.',
    '2': f'Глубоко очищающий шампунь DEEP CLEANSING для всех типов волос, 400мл.',
    '3': f'Терапевтический шампунь против выпадения волос HAIR LOSS, 400мл.\n\nСоздан на основе натуральных ингредиентов для волос всех типов.',
    '4': f'Терапевтический шампунь против перхоти DANDRUFF, 400мл.\n\nСоздан на основе натуральных ингредиентов специально для волос всех типов.',
    '5': f'Восстанавливающий шампунь REPAIR, 400мл.\n\nСоздан на основе натуральных ингредиентов специально для сухих, поврежденных, средних и толстых волос.',
    '6': f'Терапевтический шампунь VOLUME, 400мл.\n\nСоздан на основе натуральных ингредиентов специально для тонких ослабленных и лишенных объема волос.'}


LEXICON_SSR_PRICE: dict[str, str] = {
    '1': '3000',
    '2': '3000',
    '3': '3000',
    '4': '3000',
    '5': '3000',
    '6': '3000'}


LEXICON_SSR_PHOTO: dict[str, str] = {
    '1': 'https://sun9-32.userapi.com/efkzwHjZjeMThx5QM4QqiEgV9m5Sx5xR_BRGhQ/PkHsGuyVCKk.jpg',
    '2': 'https://sun9-59.userapi.com/UYi1WpsD54L_01E2nSMzAcRWR6dYAdux2S9FGQ/Ig0Khh-e_18.jpg',
    '3': 'https://sun9-16.userapi.com/EvomtwZ8moChVlKmiyMTRVxOTKIeDIFY3IQF_w/zpx8hZDy1mg.jpg',
    '4': 'https://sun9-42.userapi.com/EpZHSOCzi5LiM0T-ErpZjrpaS4DwMp-6O2Odxw/cU-6zQtNoT0.jpg',
    '5': 'https://sun9-65.userapi.com/XtRINVo9uX9CWrzCDiyXsIqKUoMGbvZQ8qWh_w/T2rJZ8CzRg0.jpg',
    '6': 'https://sun9-1.userapi.com/mCDzVJ5t5HemAiwxdPkExJw9Rv3ida0GPj-WIA/JufHobNJ1RQ.jpg'}


LEXICON_MSR_NAME: dict[str, str] = {
    '1': f'Терапевтическая разглаживающая маска SMOOTH, 500мл.\n\nСодержит кондиционирующие протеины, которые в кислой среде отлично выравнивают и сглаживают пористость.',
    '2': f'Терапевтическая восстанавливающая маска REPAIR, 500мл.\n\nСоздана на основе натуральных компонентов специально для сухих, пористых и жестких волос, которые были сильно повреждены в результате завивки или выпрямления, обесцвечивания или окрашивания, слишком частого термического воздействия.',
    '3': f'Терапевтическая маска VOLUME, 500мл.\n\nСоздана на основе натуральных компонентов специально для тонких ослабленных, редких и лишенных объема волос, сильно поврежденных при горячей укладке или в результате частых окрашиваний'}


LEXICON_MSR_PRICE: dict[str, str] = {
    '1': '4700',
    '2': '4700',
    '3': '4700'}


LEXICON_MSR_PHOTO: dict[str, str] = {
    '1': 'https://sun9-71.userapi.com/W4iRViBbH3077iCAwAKhe4DRCY6S0ragn-j2ww/BIU5bOYteYA.jpg',
    '2': 'https://sun9-63.userapi.com/B4hYq-F_RE309DQfNydjDWe3FnVdxwypFJegPg/kiZ6dIwtnxU.jpg',
    '3': 'https://sun9-71.userapi.com/iaih2LPyQFa_1vSZKL0zglBSAC9SMnkS65kvZg/Pq-yTHvilLM.jpg'}


LEXICON_CSR_NAME: dict[str, str] = {
    '1': f'Терапевтический увлажняющий кондиционер MOISTURE, 400мл.\n\nСоздан на основе натуральных ингредиентов для волос всех типов.',
    '2': f'Шелковый глубокий кондиционер для волос SILK, 400мл.\n\nПридает здоровый и ухоженный вид даже сухим, ломким и жестким волосам.'}


LEXICON_CSR_PRICE: dict[str, str] = {
    '1': '3000',
    '2': '3000'}


LEXICON_CSR_PHOTO: dict[str, str] = {
    '1': 'https://sun9-21.userapi.com/oV0D9Qwl87NAEoFnBNbW35LQvo-s7ouBfNALUg/HfDnSjO-SRs.jpg',
    '2': 'https://sun9-42.userapi.com/p1fEL33INBG6tLj-B8RE8tQaE00Hf5wthnGZew/ShEdKj36PkU.jpg'}


LEXICON_IND_NAME: dict[str, str] = {
    '1': f'Жидкий эликсир OI, 300мл.\n\nПродукт для тех, кто хочет сделать волосы ультраблестящими – быстро! Мгновенно создает эффект шелковистости за счет своей необычной жидкой текстуры и составу, богатому увлажняющими агентами.',
    '2': f'Многофункциональное молочко для волос OI, 135мл.\n\nСодержит масло аннато, провитамин B5 и функциональный аминокомплекс, который великолепно кондиционирует волосы, оставляя мягкими, защищает их от стресса и повреждений в результате термического воздействия.',
    '3': f'Масло OI для абсолютной красоты волос, 135мл.\n\nПитает локоны, создавая защитную пленку. Делает волосы блестящими и защищенными, не утяжеляя их. Помогает распутывать волосы и смягчает грубые кудрявые волосы. Сокращает время высушивания волос.',
    '4': f'Несмываемый спрей VOLU, 250мл.\n\nПридает волосам объем от самых корней. Не утяжеляет волосы, оставляя их мягкими и блестящими. Спрей придает локонам плотность и объем.',
    '5': f'Крем для усиления завитка LOVE, 150мл.\n\nПридает эластичность и четкую форму локонам. Невидим на волосах, не оставляет налет и сохраняет волосы мягкими и блестящими.',
    '6': f'Термозащитный несмываемый спрей MELU, 250мл.\n\nЭффективно защищает волосы от повреждений, полученных при применении фена и утюжка.',
    '7': f'Флюид NATURAL TECH NOURISHING, 100мл.\n\nПредназначен для сухих и ломких волос любого типа. Несмываемые флюид запечатывает кератин в кутикуле волоса, тем самым улучшая и продлевая действие всех питательных уходовых средств серии Nourishing. Легкая формула флюида обеспечивает волосам дополнительную мягкость, не утяжеляя их.',
    '8': f'Легкое несмываемое солнцезащитное молочко SU, 135мл.\n\nИдеальный экспресс-уход для всех типов волос. Прекрасно кондиционирует, увлажняет и дисциплинирует волосы после мытья. Облегчает расчесывание, придает блеск и объем без утяжеления волос.',
    '9': f'Флюид Heart of Glass, 150мл.\n\nЗапечатывает действие уходовых продуктов серии, восстанавливает повреждённые участки волоса и защищает их от ломкости. Имеет мгновенный, а также накопительный эффект, укрепляя кутикулу волоса и придавая локонам дополнительный блеск и мягкость с каждым нанесением.',
    '10': f'Несмываемая сыворотка MINU, 150мл.\n\nДеликатно ухаживает, сохраняя цвет окрашенных волос и придаёт волосам блеск и шелковистость.',
    '11': f'Универсальный несмываемый крем MOMO, 150мл.\n\nДеликатно увлажняет волосы. Придает локонам блеск и шелковистость.',
    '12': f'Восстанавливающий спрей LOVE для волнистых или кудрявых волос, 250мл.\n\nДеликатная формула спрея контролирует кудри между процедурами мытья головы, придавая волосам жизненную силу и эластичность. Восстанавливает объем и форму локонов, придавая им естественный вид и мягкость.',
    '13': f'Праймер для усиления завитка LOVE, 150мл.\n\nБлагодаря влагостойкому эффекту помогает поддерживать эластичность и четко очерченную форму локонов без пересушивания и утяжеления.',
    '14': f'Деликатный несмываемый кондиционер-спрей DEDE, 250мл.\n\nБережно ухаживает за волосами и подходит для ежедневного применения.',
    '15': f'Разглаживающий крем LOVE, 150мл.\n\nБережно разглаживает волнистые волосы. Придает локонам эластичность и объем.',
    '16': f'Несмываемый крем для укрощения очень кудрявых волос LOVE, 150мл.\n\nНевидим на волосах, сокращает чрезмерный объем кудрявых волос, оставляя их мягкими и блестящими. Не перегружает волосы и не оставляет налет.',
    '17': f'Дисциплинирующая несмываемая сыворотка LOVE, 150мл.\n\nОбладает эффектом термозащиты и антифриз, значительно облегчает выпрямление локонов утюжком. Способствует дополнительному питанию, мягкости и добавляет блеск волосам.',
    '18': f'Кератиновый крем VITA BOOSTER, 75мл.\n\nПредотвращает разрушение кератина и последующее вымывание его из волос. Помогает справиться с секущимися кончиками и предотвращает пушение волос.'}


LEXICON_IND_PRICE: dict[str, str] = {
    '1': '4300',
    '2': '3400',
    '3': '5700',
    '4': '3800',
    '5': '3000',
    '6': '4300',
    '7': '3800',
    '8': '2700',
    '9': '3500',
    '10': '2700',
    '11': '3000',
    '12': '3000',
    '13': '3000',
    '14': '3500',
    '15': '3000',
    '16': '3000',
    '17': '3000',
    '18': '1350'}


LEXICON_IND_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2022/05/foto-produkta.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2019/03/oi-mnogofunkczionalnoe-molochko-dlya-volos.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2019/03/oi-maslo-dlya-absolyutnoj-krasoty-volos-s-maslom-annatto.jpg',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2019/04/volu-nesmyvaemyj-sprej-dlya-pridaniya-obema-volosam.jpg',
    '5': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-27.jpg',
    '6': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-39.jpg',
    '7': 'https://cdn.davines.ru/wp-content/uploads/2020/01/nt-nourishing-pitatelnyj-flyuid-zapechatyvayushhij-keratin.jpg',
    '8': 'https://cdn.davines.ru/wp-content/uploads/2019/04/su-solnczezashhitnoe-molochko.jpg',
    '9': 'https://cdn.davines.ru/wp-content/uploads/2021/04/72008_heartofglass_sheerglaze_150ml_davines_2000x-1-1.jpg',
    '10': 'https://cdn.davines.ru/wp-content/uploads/2019/04/new-project-4146.jpg',
    '11': 'https://cdn.davines.ru/wp-content/uploads/2019/04/momo-uvlazhnyayushhij-kondiczioner-1.jpg',
    '12': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-28.jpg',
    '13': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-29.jpg',
    '14': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-19.jpg',
    '15': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-23.jpg',
    '16': 'https://cdn.davines.ru/wp-content/uploads/2020/01/new-project-2019-10-09t121728.250.jpg',
    '17': 'https://cdn.davines.ru/wp-content/uploads/2022/08/love-smoothing-p.jpg',
    '18': 'https://sun9-56.userapi.com/impg/zTIr8XrvLu5kQBeLNy6XLilleGCp5L8bFrunFA/kl-eJsJSAow.jpg?size=807x538&quality=96&sign=8aa6857e9a141db44eefb66d4f79bccf&c_uniq_tag=Uc1BmIV5aJ9mPgSA0CJ4A_wb-9oOuYHYrX2P4EuhCHo&type=none'}


LEXICON_SKIN_NAME: dict[str, str] = {
    '1': f'Очищающий гель NATURAL TECH PURIFYING, 150мл.\n\nУхаживает за кожей головы и борется с сухой или жирной перхотью.',
    '2': f'Глубоко очищающая паста-скраб для всех типов волос и кожи головы SOLU, 250мл.\n\nУдаляет вредные вещества, которые скапливаются в волосах и коже головы из-за плохой экологии. Освежает кожу головы, дарит волосам чистоту и энергию на долгое время. Дополнительно придает текстуру волосам.',
    '3': f'Очищающий уход для баланса кожи головы NT Rebalancing, 250мл.\n\nДля жирной кожи головы с избыточной выработкой нежелательного себума. Смываемый косметический уход эффективно очищает волосы и кожу головы от излишка себума. Придаёт мгновенное ощущение свежести.',
    '4': f'Регенерирующий гель NATURAL TECH ENERGIZING, 150мл.\n\nСоздан специально для ухода за кожей головы и хрупкими истонченными волосами, склонными к выпадению. Укрепляет волосы, служит для профилактики сезонного выпадения волос, замедляет процесс облысения. Придает энергию и плотность тонким и слабым волосам. Обладает легким стайлинговым эффектом.'}


LEXICON_SKIN_PRICE: dict[str, str] = {
    '1': '3000',
    '2': '3300',
    '3': '2500',
    '4': '3500'}


LEXICON_SKIN_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2019/04/nt-purifying-ochishhayushhij-gel-protiv-perhoti.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2022/02/solu-scrub.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2021/10/8385_naturaltech_rebalancing_cleansing_treatment_250ml_davines.png',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2019/04/energeticheskij-gel.jpg'}


LEXICON_TIN_NAME: dict[str, str] = {
    '1': f'Оттеночный шампунь Alchemic (Серебро), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы. Позволяет устранить желтизну на предварительно осветленных волосах, окрашенных в оттенок платинового блонда, а так же седых волосах, смягчая их и защищая от повреждения.',
    '2': f'Оттеночный шампунь Alchemic (Шоколад), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы, защищая их от повреждения и придавая шелковистость.',
    '3': f'Оттеночный шампунь Alchemic (Табак), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы средне- и темно-коричневых оттенков, смягчая их и защищая от повреждения.',
    '4': f'Оттеночный шампунь Alchemic (Медь), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы, защищая их от повреждения и придавая шелковистость.',
    '5': f'Оттеночный шампунь Alchemic (Золото), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы, защищая их от повреждения и придавая шелковистость.',
    '6': f'Оттеночный шампунь Alchemic (Красный), 280мл.\n\nБлагодаря мягким поверхностно-активным веществам, полученным из натуральных ингредиентов, и провитамину В5 (пантенолу) деликатно очищает, питает и увлажняет волосы, защищая их от повреждения и придавая шелковистость.',
    '7': f'Деликатный кондиционер Alchemic (Серебро), 250мл.\n\nБлагодаря маслу жожоба глубоко питает и увлажняет волосы, делая их шелковистыми и блестящими. Устраняет нежелательную желтизну на предварительно осветленных волосах, а также седых волос, смягчая их и защищая от повреждения.',
    '8': f'Деликатный кондиционер Alchemic (Шоколад), 250мл.\n\nУсиливает естественный цвет волос и освежает коричневый оттенок окрашенных волос. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '9': f'Деликатный кондиционер Alchemic (Медь), 250мл.\n\nПридает теплый медный оттенок натуральным волосам и поддерживает яркость медных оттенков окрашенных волос. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '10': f'Деликатный кондиционер Alchemic (Табак), 250мл.\n\nУсиливает естественный цвет волос и поддерживает яркость окрашенных волос. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '11': f'Кондиционер ALCHEMIC (Розовый), 250мл.\n\nСоздает креативный розовый оттенок на волосах. Подходит для светлых натуральных (желательно блонд/светлый блонд и светлее), а также для осветленных и обесцвеченных волос для создания модных цветовых эффектов. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '12': f'Оттеночный кондиционер Alchemic (Золото), 250мл.\n\nУсиливает светло-золотистые или медово-золотистые оттенки натуральных и окрашенных волос. Благодаря входящим в состав аминокислотам и мягким поверхностно-активным веществам, глубоко питает и увлажняет волосы, защищая их от повреждения и придавая эластичность.',
    '13': f'Деликатный кондиционер Alchemic (Красный), 250мл.\n\nПридает красноватый оттенок натуральным волосам и поддерживает яркость красных оттенков окрашенных волос. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '14': f'Кондиционер ALCHEMIC (Лавандовый), 250мл.\n\nСоздает креативный лавандовый оттенок на волосах. Подходит для светлых натуральных (желательно блонд/светлый блонд и светлее), а также для осветленных и обесцвеченных волос для создания модных цветовых эффектов. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '15': f'Кондиционер ALCHEMIC (Коралл), 250мл.\n\nСоздает креативный коралловый оттенок на волосах. Подходит для светлых натуральных (желательно блонд/светлый блонд и светлее), а также для осветленных и обесцвеченных волос для создания модных цветовых эффектов. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '16': f'Кондиционер ALCHEMIC (Приглушенный синий), 250мл.\n\nСоздает креативный синий оттенок на волосах. Подходит для светлых натуральных (желательно блонд/светлый блонд и светлее), а также для осветленных и обесцвеченных волос для создания модных цветовых эффектов. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.',
    '17': f'Кондиционер ALCHEMIC (Морская волна), 250мл.\n\nСоздает креативный оттенок морской волны на волосах. Подходит для светлых натуральных (желательно блонд/светлый блонд и светлее), а также для осветленных и обесцвеченных волос для создания модных цветовых эффектов. Благодаря маслу жожоба глубоко питает, смягчает и увлажняет волосы, делая их шелковистыми и блестящими.'}

LEXICON_TIN_PRICE: dict[str, str] = {
    '1': '2300',
    '2': '2300',
    '3': '2300',
    '4': '2300',
    '5': '2300',
    '6': '2300',
    '7': '3150',
    '8': '3150',
    '9': '3150',
    '10': '3150',
    '11': '3150',
    '12': '3150',
    '13': '3150',
    '14': '3150',
    '15': '3150',
    '16': '3150',
    '17': '3150'}


LEXICON_TIN_PHOTO: dict[str, str] = {
    '1': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-serebro.jpg',
    '2': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-shokolad6.jpg',
    '3': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-tabak.jpg',
    '4': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-med.jpg',
    '5': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-zoloto.jpg',
    '6': 'https://cdn.davines.ru/wp-content/uploads/2019/04/ottenochnyj-shampun-alhimik-krasnyj.jpg',
    '7': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik-serebro.jpg',
    '8': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik-shokolad-1.jpg',
    '9': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik-med.jpg',
    '10': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik-tabak.jpg',
    '11': 'https://cdn.davines.ru/wp-content/uploads/2020/02/alhimik-rozovyj.jpg',
    '12': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik-zoloto.jpg',
    '13': 'https://cdn.davines.ru/wp-content/uploads/2019/04/kondiczioner-alhimik.jpg',
    '14': 'https://cdn.davines.ru/wp-content/uploads/2020/02/alhimik-lavandovyj.jpg',
    '15': 'https://cdn.davines.ru/wp-content/uploads/2020/02/alhimik-korallovyj-2.jpg',
    '16': 'https://cdn.davines.ru/wp-content/uploads/2020/02/ahimik-goluboj.jpg',
    '17': 'https://cdn.davines.ru/wp-content/uploads/2020/02/alhimik-priglushennyj-sinij.jpg'}
