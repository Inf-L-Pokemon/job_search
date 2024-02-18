import urllib

from src.vac_from_api import HeadHunterAPI
from src.vac_json import VacJSON
from urllib.parse import unquote_plus


def main():
    start = int(input("Вы хотите осуществить поиск по вакансиям с ресурса HeadHunter или у вас уже есть файл с "
                      "вакансиями?\n1 - Поиск новых вакансий\n2 - Работа с существующим файлом\n3 - Выход из "
                      "программы\n"))
    if start == 1:
        text = input("Введите слово или словосочетание для поиска вакансий.\n")
        vac = HeadHunterAPI(text)
        response = vac.get_vac_from_api()
        print(f"Найдено {response['found']} вакансий.")

        save_answer = int(
            input("Хотите сохранить данные вакансии в файл для последующей работы с ними?\n1 - Да\n2 - Нет\n"))
        if save_answer == 1:
            vac_to_json = VacJSON(response)
            vac_to_json.add_vac()
        elif save_answer == 2:
            pass
        else:
            quit("Неверно введен ответ.")

    elif start == 2:
        pass
    elif start == 3:
        quit()
    else:
        quit("Неверно введен ответ.")

    vac = VacJSON()
    vac_from_json = vac.get_vac_from_file()
    req_all = vac_from_json["alternate_url"]
    req = req_all[req_all.find("text=") + 5:]
    print(f"""Данная подборка вакансий создана по запросу "{urllib.parse.unquote_plus(req, encoding='utf-8')}". 
    Количество вакансий по данному запросу - {vac_from_json['found']}""")



if __name__ == '__main__':
    main()
