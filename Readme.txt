Ссылка на скрипт:
https://raw.githubusercontent.com/Krugger1982/Test-exercises/main/main.py

Программа вызывает окно с виджетами для поиска вакансий на сайте HH.ru.
Предлагается заполнить форму с несколькими полями.
После заполнения - кнопка "Искать"(запускает собственно скрипт) или кнопка "Очистить" (обнуляет все поля формы)

Программа:
- создает запросы для получения из справочника значения id указанного региона (если указан маленький город в области, но этот город есть в списке грдов справочника, 
  то будет возвращен id всего региона, чтобы пользователь видел результаты поиска и в областном центре, и в соседних городах области)
  (это 1й запрос на API)
- преобразует значения "опыт работы" и "образование" в параметры для поиска,
- Формирует список параметров для поиска
- Создает и направляет запрос на API для поиска вакансий по собранным параметрам (это второй запрос)
- Полученный ответ преобразуется в JSON.
- Создается файл preliminary_data.json в текущей директории
- в файл дописывается результат поиска - информация о вакансиях

Использовались библиотеки:
tkinter - для создания виджета
json - для разбора и работы с json-форматом данных
requests - для формирования запроса на адрес
time - для временной задержки, чтоб не сайт hh.ru не выкинул за слишком частые запросы


На работу ушло примерно 8 часов. 
Трудности составила работа с tkinter (пришлось много гуглить и разбираться с основами), а также тестироание - пока все заработало.
