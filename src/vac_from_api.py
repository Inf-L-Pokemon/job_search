import requests

from src.abs_class import VacAPI


class HeadHunterAPI(VacAPI):
    """
    Получение данных о вакансиях из API HeadHunter.
    """

    def __init__(self, text):
        self.__text = text
        self.page = 0
        self.per_page = 50
        self.__basic_url = "https://api.hh.ru/vacancies"

    def get_vac_from_api(self):

        params = {"text": self.__text, "page": self.page, "per_page": self.per_page}
        response = requests.get(self.__basic_url, params=params)
        vac_json = response.json()

        while self.page < vac_json["pages"] - 1:
            self.page += 1
            response = requests.get(
                self.__basic_url,
                params={
                    "text": self.__text,
                    "page": self.page,
                    "per_page": self.per_page,
                },
            )
            vac_json["items"].extend(response.json()["items"])

        return vac_json
