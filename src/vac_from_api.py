import requests

from src.abs_class import VacAPI
from pprint import pprint


class HeadHunterAPI(VacAPI):
    """
    Получение данных о вакансиях из API HeadHunter.
    """

    def __init__(self, name):
        self.__name = name
        self.__basic_url = "https://api.hh.ru/vacancies"

    def get_vac_from_api(self):

        params = {"text": self.__name,
                  "per_page": 10}

        response = requests.get(self.__basic_url, params=params).json()

        return response


if __name__ == '__main__':
    vac = HeadHunterAPI("Python junior")
    pprint(vac.get_vac_from_api())