import json

from src.abs_class import VacFile


class VacJSON(VacFile):
    """
    Сохранение, удаление вакансий в JSON файл. Получение вакансий из JSON файла.
    """

    def __init__(self, vac_json=None):
        self.vac_json = vac_json

    @staticmethod
    def get_vac_from_file():
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as data:
                vac_from_json = json.load(data)
        except Exception:
            quit("Файл не существует или поврежден")

        list_vac = []
        for vac in vac_from_json["items"]:
            list_vac.append(vac)

        return list_vac

    @staticmethod
    def del_vac():
        with open("data/vacancies.json", "w", encoding="utf-8") as data:
            pass

    def add_vac(self):
        with open("data/vacancies.json", "w", encoding="utf-8") as data:
            json.dump(self.vac_json, data, ensure_ascii=False)

    @staticmethod
    def get_all_req():
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as data:
                vac_from_json = json.load(data)
                return vac_from_json
        except Exception:
            quit("Файл не существует или поврежден")
