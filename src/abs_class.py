from abc import ABC, abstractmethod


class VacAPI(ABC):
    """
    Абстрактный класс для подключения к API с вакансиями и получения вакансий.
    """

    @abstractmethod
    def get_vac_from_api(self):
        pass


class VacFile(ABC):
    """
    Абстрактный класс для работы с файлом вакансий.
    """

    @abstractmethod
    def add_vac(self):
        pass

    @abstractmethod
    def get_vac_from_file(self):
        pass

    @abstractmethod
    def del_vac(self):
        pass
