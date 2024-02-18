import json

from src.abs_class import VacFile


class VacJSON(VacFile):
    """
    Сохранение, удаление вакансий в JSON файл. Получение вакансий из JSON файла по заданным параметрам.
    """

    def __init__(self, vac_json=None):
        self.vac_json = vac_json

    def get_vac_from_file(self):
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as data:
                vac_from_json = json.load(data)
                return vac_from_json
        except Exception:
            quit("Файл не существует или поврежден")

    def del_vac(self):
        with open("data/vacancies.json", "w", encoding="utf-8") as data:
            pass

    def add_vac(self):
        with open("data/vacancies.json", "w", encoding="utf-8") as data:
            json.dump(self.vac_json, data, ensure_ascii=False)
