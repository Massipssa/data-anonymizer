from abc import ABC, abstractmethod
from typing import Optional, Dict


ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP: Dict[str, str] = {
    "ColumnSuppression": "suppression",
    "NumericalPerturbation": "numerical_perturbation",
    "KAnonymity": "k_anonymity"
}


class Anonymization(ABC):

    def __init__(self, algorithm_name: str, id: Optional[str] = None):
        self._algorithm_name = algorithm_name
        self._id = id

    @property
    def algorithm_name(self) -> str:
        return self._algorithm_name

    @abstractmethod
    def anonymize(self):
        raise NotImplementedError
