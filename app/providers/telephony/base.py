from abc import ABC, abstractmethod


class TelephonyProvider(ABC):
    @abstractmethod
    def initiate_call(self, to_number: str, from_number: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def end_call(self, call_id: str) -> dict:
        raise NotImplementedError
