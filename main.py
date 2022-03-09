import tkinter as tk
from tkinter import ttk
import json
import requests
import time

def clear():
    entry_keywords.delete(0, tk.END)
    entry_town.delete(0, tk.END)
    comboEducations.current(0)
    comboExperience.current(0)

def search():
    """ Организует поисковый запрос на публичный API сайта HH и результаты записывает в файлы в текущей директории
    """
#    profession - entry_profession.get()
    profession = "1.10"
    keyw = entry_keywords.get()
    town = entry_town.get()
    education_level = comboEducations.current()
    experience_level = comboExperience.current()
    parametres = {'text':keyw,
                  'experience':expirience_establishing(experience_level),
                  'area':find_area(town),
                  'specialization':'1.10',
                  'education_level':education_establishing(education_level),
                  'per_page': 100 # Кол-во вакансий на 1 странице
                 }
    for page in range(20):                  # берем первые 2000 ответов
        parametres['page']= page            # добавляем номер страницы
        req = requests.get('https://api.hh.ru/vacancies', parametres)           # Посылаем запрос к API
        data = req.content.decode()                                             # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()


        data = json.loads(data)
        with open('preliminary_data.json', mode='a', encoding='utf8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        file.close()

        # проверка на случай если вакансий меньше чем 2000
        
        if (data['pages'] - page) <= 1:
            break

    time.sleep(0.25)
    
def find_area(town):
    """ находит id указанного города (или области в РФ)
    """
    def find_town(region, TownName):
        """ Если в регионе есть города, представленные на HH то поищем среди них
        """
        for area in region:
            if area["name"] == TownName:
                return True           
        return False
    
    json_areas = json.loads(requests.get('https://api.hh.ru/areas').text)
    for country in json_areas:
        if country["name"] == "Россия":
            for region in country["areas"]:
                if region["name"] == town or find_town(region["areas"], town):
                    return region["id"]
                
    

def expirience_establishing(experience_level):
    exp = ["noExperience", "between1And3", "between3And6", "moreThan6"]
    return exp[experience_level]

def education_establishing(education_level):
    educs = ["secondary", "special_secondary", "unfinished_higher",  "higher", "bachelor", "master", "candidate", "doctor"]
    return educs[education_level]

window = tk.Tk()
frame_greetings = tk.Frame()
label_greetings = tk.Label(master = frame_greetings, text="Здравствуйте! \n Сейчас мы попытаемся поискать вакансию на hh.ru",
                 foreground="black",  # Устанавливает белый текст
                 background="cornsilk3",  # Устанавливает серый фон
                 width=50,
                 height=4)
label_greetings.pack(padx=5, pady=5)

frame_profession= tk.Frame()
label_profession = tk.Label(master=frame_profession, text="Введите название профессии")
label_profession.pack(padx=5, pady=5)
##entry_profession = tk.Entry(master=frame_profession)
##entry_profession.pack(fill=tk.X, padx=5, pady=5)
# Временно вставим заглушку - единственный вид профессии - вебмастер
combo_prof = ttk.Combobox(master=frame_profession, values=["Web мастер"])
combo_prof.pack(fill=tk.X)
combo_prof.current(0)   # устанавливаем по умолчанию на первое значение



frame_keywords= tk.Frame()
label_keywords = tk.Label(master=frame_keywords, text="Введите ключевые слова через пробел (для поиска)")
label_keywords.pack(padx=5, pady=5)
entry_keywords = tk.Entry(master=frame_keywords)
entry_keywords.pack(fill=tk.X, padx=5, pady=5)



frame_town= tk.Frame()
label_town = tk.Label(master=frame_town, text="Введите город поиска")
label_town.pack(padx=5, pady=5)

entry_town = tk.Entry(master=frame_town)
entry_town.pack(fill=tk.X, padx=5, pady=5)




frame_education= tk.Frame()
labelTop = tk.Label(master=frame_education,text = "Выберите ваш уровень образования")
labelTop.pack(fill=tk.X, padx=5, pady=5)

comboEducations = ttk.Combobox(master=frame_education, values=[    "Среднее", 
                                                                "Среднее специальное",
                                                                "Неоконченное высшее",
                                                                "Высшее",
                                                                "Бакалавр",
                                                                "Магистр",
                                                                "Кандидат наук",
                                                                "Доктор наук"
                                                                ])
comboEducations.pack(fill=tk.X)
comboEducations.current(0)# устанавливаем по умолчанию на первое значение

frame_experience= tk.Frame()
labelTop = tk.Label(master=frame_experience,text = "Выберите ваш опыт работы в этой должности")
labelTop.pack(fill=tk.X, padx=5, pady=5)

comboExperience = ttk.Combobox(master=frame_experience, values=[    "Нет опыта",
                                                                 "От 1 до 3 лет",
                                                                 "От 3 до 6 лет",
                                                                 "Более 6 лет"
                                                                ])
comboExperience.pack(fill=tk.X)
comboExperience.current(0)

frame_greetings.pack(fill=tk.X)
frame_profession.pack(fill=tk.X)
frame_keywords.pack(fill=tk.X)
frame_town.pack(fill=tk.X)
frame_education.pack(fill=tk.X)
frame_experience.pack(fill=tk.X)


# Создает новую рамку `frm_buttons` для размещения
# кнопок "Искать" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
 
# Создает кнопку "Искать" и размещает ее
# в правой части рамки `frm_buttons`.
btn_search = tk.Button(master=frm_buttons, text="Искать", command=search)
btn_search.pack(side=tk.RIGHT, padx=10, ipadx=10)
 
# Создает кнопку "Очистить" и размещает ее
# с правой части от оставшейся площади `frm_buttons`.
btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
btn_clear.pack(side=tk.RIGHT, ipadx=10)


window.mainloop()
