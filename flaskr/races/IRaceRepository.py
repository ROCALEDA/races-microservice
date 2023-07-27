from abc import ABC, abstractmethod


class IRaceRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass
