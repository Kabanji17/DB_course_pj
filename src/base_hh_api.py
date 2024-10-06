from abc import ABC, abstractmethod


class BaseHeadHunterAPI(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def __init__(self, file_worker: str):
        """Атрибут в конструкторе для явного указания пути до файла, куда можно сохранить данные"""
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self) -> object:
        """Метод загрузки вакансий и сохранения в List[dict]"""
        pass
