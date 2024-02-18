import urllib
from pprint import pprint
from urllib.parse import unquote_plus

from src.vac_from_api import HeadHunterAPI
from src.vac_json import VacJSON
from src.work_with_vac import Vacancies


def main():
    start = input(
        "Вы хотите осуществить поиск по вакансиям с ресурса HeadHunter или у вас уже есть файл с "
        "вакансиями?\n1 - Поиск новых вакансий\n2 - Работа с существующим файлом\n3 - Выход из "
        "программы\n"
    )
    if int(start) == 1:
        text = input("Введите слово или словосочетание для поиска вакансий.\n")
        vac = HeadHunterAPI(text)
        response = vac.get_vac_from_api()
        print(f"Найдено {response['found']} вакансий.")

        save_answer = int(
            input(
                "Хотите сохранить данные вакансии в файл для последующей работы с ними?\n1 - Да\n2 - Нет\n"
            )
        )
        if save_answer == 1:
            vac_to_json = VacJSON(response)
            vac_to_json.add_vac()
        elif save_answer == 2:
            quit()
        else:
            quit("Неверно введен ответ.")

    elif int(start) == 2:
        pass
    elif int(start) == 3:
        quit()
    else:
        quit("Неверно введен ответ.")

    vac_from_json = VacJSON.get_all_req()
    req_all = vac_from_json["alternate_url"]
    req = req_all[req_all.find("text=") + 5 :]
    print(
        f"""Данная подборка вакансий создана по запросу "{urllib.parse.unquote_plus(req, encoding='utf-8')}"."""
    )
    print(f"Количество вакансий по данному запросу - {vac_from_json['found']}")

    key_top_vac = input(
        "Введите количество вакансий для отображения (топ по зарплате)\n"
    )

    Vacancies.instantiate_from_list_vac(VacJSON.get_vac_from_file())

    top_vac = sorted(Vacancies.all, reverse=True)[: int(key_top_vac)]
    for vac in top_vac:
        pprint(vac)


if __name__ == "__main__":
    main()
