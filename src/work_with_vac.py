


class Vacancies:
    """
    Класс работы с вакансиями
    """

    all = []

    def __init__(self, name, url, salary_from, salary_to, description, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.experience = experience
        self.all.append(self)

    def __repr__(self):
        return (
            f'Вакансия: {self.name}\n'
            f'Ссылка на вакансию: {self.url}\n'
            f'Зарплата: От {self.salary_from} до {self.salary_to}\n'
            f'Описание: {self.description}\n'
            f'Опыт работы: {self.experience}\n'
        )

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    @classmethod
    def instantiate_from_list_vac(cls, list_vac):
        cls.all = []
        for vac in list_vac:
            Vacancies(name=vac["name"], url=vac["alternate_url"], salary_from=vac["salary"]["from"] if vac["salary"] and vac["salary"]["from"] else 0, salary_to=vac["salary"]["to"] if vac["salary"] and vac["salary"]["to"] else 0, description=vac["snippet"]["responsibility"], experience=vac["experience"]["name"])
