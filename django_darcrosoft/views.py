from django.shortcuts import render

def home(request):
    return render(request, 'page_1.html')

def page_1(request):
    slides = [
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Highlight-MultiCanvas-Microsoft-Copilot-App-3screens:VP5-1920x600',
            'heading': 'Раскройте потенциал с Darcrosoft Copilot',
            'description': 'Более быстрый результат и творчество без границ с помощью ИИ, где бы вы ни были.',
            'text_color': 'black',
        },
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Highlight-Hero-Windows11-GlobalLaunch:VP5-1920x600',
            'heading': 'Разработано для жизни — сегодня и в будущем',
            'description': 'Следующее поколение игр. Ваши цели. Друзья и семья. С Windows 11 вы станете еще ближе к тому, что успели полюбить.',
            'text_color': 'white',
        }
    ]
    cards = [
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/gldn-MSFT-CP-Edge?wid=380&hei=213&fit=crop',
            'title': 'Darcrosoft Edge',
            'description': 'Потрясающая производительность, больше конфиденциальности, продуктивности и дополнительных возможностей.',
            'button_text': 'Скачать',
        },
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/gldn-Soft-CP-OneDriveCampaignRefresh-2?wid=380&hei=213&fit=crop',
            'title': 'Darcrosoft OneDrive',
            'description': 'Сохраняйте свои файлы и фотографии на OneDrive — они будут доступны с любого устройства и где угодно.',
            'button_text': 'Подробнее',
        },
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-PC-SMB-OneNote?wid=380&hei=213&fit=crop',
            'title': 'OneNote',
            'description': 'Приведите свои заметки и дела в порядок.',
            'button_text': 'Узнать больше',
        },
        {
            'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/gldn-CP-MSCOM-Outlook-iOS-Android?wid=380&hei=213&fit=crop',
            'title': 'Outlook для iOS и Android',
            'description': 'Будьте на связи. Организовывайте. Успевайте больше.',
            'button_text': 'Скачать',
        }
    ]
    card_1 = {
        'image_url': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Hero-Highlight-Teams-Floating-UI:VP5-1596x600',
        'title': 'Больше общения с близкими',
        'description': 'Общайтесь, созванивайтесь и составляйте планы с семьей и друзьями в Darcrosoft Teams',
        'button_text': 'Подробнее',
        'button_link': '#',  # Ссылка на страницу
    }
    cards_2 = [
        {
            'image': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Visual-Studio-Icon?wid=380&hei=213&fit=crop',
            'title': 'Visual Studio 2022',
            'text': 'Наиболее комплексная среда IDE для разработчиков .NET и C++ на Windows для создания веб-приложений, приложений для ПК, облачных и мобильных приложений, а также служб и игр.',
            'button_text': 'Скачайте Visual Studio 2022'
        },
        {
            'image': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/JIC-DPS-CP01?wid=380&hei=213&fit=crop',
            'title': 'Добро пожаловать в Windows 365 Cloud PC',
            'text': 'Работать с Windows в облаке Darcrosoft теперь можно на любых устройствах.',
            'button_text': 'Попробуйте прямо сейчас'
        },
        {
            'image': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/gldn-Apps-CP-EdgeBingLifeStyle?wid=380&hei=213&fit=crop',
            'title': 'Darcrosoft Edge',
            'text': 'Производительность, совместимость, безопасность. Браузер для бизнеса.',
            'button_text': 'Скачать'
        },
        {
            'image': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Brand-Hybrid-Work?wid=380&hei=213&fit=crop',
            'title': 'Встречайте гибридный мир',
            'text': 'Попробуйте инструменты, ресурсы и стратегии, которые помогут вашим сотрудникам добиться успеха в новом мире гибкой рабочей среды.',
            'button_text': 'Подробнее'
        },
    ]
    footer_data = {
        'new_items': [
            {'text': 'Darcrosoft Copilot', 'url': '#'},
            {'text': 'Darcrosoft 365', 'url': '#'}
        ],
        'store_items': [
            {'text': 'Профиль учетной записи', 'url': '#'},
            {'text': 'Возврат товаров', 'url': '#'},
            {'text': 'Отслеживание заказа', 'url': '#'}
        ],
        'education_items': [
            {'text': 'Darcrosoft для образования', 'url': '#'},
            {'text': 'Устройства для образования', 'url': '#'},
            {'text': 'Darcrosoft Teams для образования', 'url': '#'},
            {'text': 'Darcrosoft 365 для образования', 'url': '#'},
            {'text': 'Office для образования', 'url': '#'},
            {'text': 'Подготовка и профессиональное развитие преподавателей', 'url': '#'},
            {'text': 'Специальные предложения для учащихся и родителей', 'url': '#'},
            {'text': 'Azure для учащихся', 'url': '#'}
        ],
        'business_items': [
            {'text': 'Darcrosoft Cloud', 'url': '#'},
            {'text': 'Darcrosoft Security', 'url': '#'},
            {'text': 'Azure', 'url': '#'},
            {'text': 'Dynamics 365', 'url': '#'},
            {'text': 'Darcrosoft 365', 'url': '#'},
            {'text': 'Darcrosoft Advertising', 'url': '#'},
            {'text': 'Darcrosoft 365 Copilot', 'url': '#'},
            {'text': 'Darcrosoft Teams', 'url': '#'}
        ],
        'it_items': [
            {'text': 'Центр разработчиков', 'url': '#'},
            {'text': 'Документация', 'url': '#'},
            {'text': 'Darcrosoft Learn', 'url': '#'},
            {'text': 'Сообщество Darcrosoft Tech', 'url': '#'},
            {'text': 'Azure Marketplace', 'url': '#'},
            {'text': 'AppSource', 'url': '#'},
            {'text': 'Darcrosoft Power Platform', 'url': '#'},
            {'text': 'Visual Studio', 'url': '#'}
        ],
        'company_items': [
            {'text': 'Вакансии', 'url': '#'},
            {'text': 'О корпорации Майкрософт', 'url': '#'},
            {'text': 'Инвесторы', 'url': '#'},
            {'text': 'Экологическая устойчивость', 'url': '#'}
        ],
        'footer_base': [
            {'text': 'Связаться с Darcrosoft', 'url': '#'},
            {'text': 'Конфиденциальность', 'url': '#'},
            {'text': 'Условия использования', 'url': '#'},
            {'text': 'Товарные знаки', 'url': '#'},
            {'text': 'Сведения о рекламе', 'url': '#'},
            {'text': '© Darcrosoft 2024', 'url': '#'}
        ]
    }
    context = {
        'title': 'Darcrosoft',
        'favicon_url': 'img/darcrosoft%20favicon.png',
        'css_bootstrap': 'css/bootstrap.min.css',  # Путь к файлу Bootstrap
        'custom_css': 'page_1/css/style.css',  # Путь к пользовательскому CSS
        'favicon_url': 'img/darcrosoft favicon.png',  # Путь к фавикону
        'preconnect_google': 'https://fonts.googleapis.com',  # Google Fonts
        'preconnect_gstatic': 'https://fonts.gstatic.com',  # GStatic
        'google_fonts_url': ('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap'),  # URL шрифта
        'logo_url': 'img/Darcrosoft Logo Text.png',  # Путь к логотипу
        'navbar_link_1': 'Darcrosoft 365',  # Текст первой ссылки на странице
        'navbar_link_2': 'Copilot',  # Текст второй ссылки на странице
        'dropdown_label': 'Источники',  # Текст для выпадающего меню
        'dropdown_item_1': 'Google',  # Первый пункт в выпадающем меню
        'dropdown_item_2': 'Microsoft',  # Второй пункт в выпадающем меню
        'slides': slides, # Слайды
        'cards': cards, # Карточки
        'card_1': card_1, # Карточка 1
        'business_text': 'Для бизнеса',
        'cards_2': cards_2, # Карточки 2
        'button_text': 'Назад наверх', # Текст на кнопке
        'footer_data': footer_data, # Контент футера
    }
    return render(request, 'page_1.html', context)

def page_2(request):

    context = {
        'title': 'Darcrosoft',
        'favicon_url': 'img/darcrosoft%20favicon.png',
        'css_bootstrap': 'css/bootstrap.min.css',  # Путь к файлу Bootstrap
        'custom_css': 'page_2/css/style.css',  # Путь к пользовательскому CSS
        'favicon_url': 'img/darcrosoft favicon.png',  # Путь к фавикону
        'preconnect_google': 'https://fonts.googleapis.com',  # Google Fonts
        'preconnect_gstatic': 'https://fonts.gstatic.com',  # GStatic
        'google_fonts_url': ('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap'), # URL шрифта
        'logo_url': 'img/Darcrosoft Logo Text.png',  # Путь к логотипу
        'navbar_links': [  # Ссылки навигационной панели
            {'name': 'Darcrosoft 365', 'url': 'page_2', 'is_active': True},
            {'name': 'Планы и цены', 'url': 'page_2', 'is_active': False},
        ],
        'dropdown_label': 'Продукты',  # Название выпадающего меню
        'dropdown_items': [  # Элементы выпадающего меню
            {'name': 'Для дома', 'url': '#'},
            {'name': 'Для бизнеса', 'url': '#'},
        ],
        'search_placeholder': 'Поиск',  # Placeholder для поля поиска
        'search_button_text': 'Найти',  # Текст кнопки поиска
        'regions': [  # Список регионов для выбора
            {'code': 'ru', 'name': 'Россия'},
            {'code': 'by', 'name': 'Беларусь'},
            {'code': 'kz', 'name': 'Казахстан'},
            {'code': 'kg', 'name': 'Киргизия'},
            {'code': 'tj', 'name': 'Таджикистан'},
            {'code': 'tm', 'name': 'Туркмения'},
            {'code': 'uz', 'name': 'Узбекистан'},
        ],
        'hero_image': 'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Hero-Backgroundimage-1600x680?resMode=sharp2&op_usm=1.5,0.65,15,0&wid=1600&qlt=100&fit=constrain',
        'main_heading': 'Добейтесь нового уровня продуктивности с ИИ',
        'sub_heading': 'Получите приложения для продуктивной работы, систему безопасности и хранилище в Microsoft 365. Затем добавьте возможности ИИ с помощью Copilot Pro.',
        'button_plan_price': 'Планы и цены',
        'button_try_free': 'Попробовать бесплатно',
        'tabs': [
            {'name': 'Для дома', 'url': '#'},
            {'name': 'Для бизнеса', 'url': '#'},
            {'name': 'Для крупных предприятий', 'url': '#'},
            {'name': 'Для образования', 'url': '#'},
        ],
        'sticky_nav_items': [
            {'name': 'Как это работает', 'url': '#'},
            {'name': 'Подборка новостей', 'url': '#'},
            {'name': 'Состав решения', 'url': '#'},
            {'name': 'Планы', 'url': '#'},
            {'name': 'Истории клиентов', 'url': '#'},
        ],
        'sticky_button_plan_price': 'Планы и цены',
        'sticky_button_try_free': 'Попробовать бесплатно',
    }
    return render(request, 'page_2.html', context)
