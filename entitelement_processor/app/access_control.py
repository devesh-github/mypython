from abc import ABC, abstractmethod
from typing import List

class BaseResource(ABC):
    @abstractmethod
    def is_user_allowed(self, predefined_allowlist: List[str]) -> bool:
        pass

class BaseAccessControl(ABC):
    @abstractmethod
    def get_accessible_resources(self, resources: List[BaseResource], predefined_allowlist: List[str]) -> List[str]:
        pass

class Resource(BaseResource):
    def __init__(self, name: str, allowlist: List[str]):
        self.name = name
        self.allowlist = allowlist

    def is_user_allowed(self, predefined_allowlist: List[str]) -> bool:
        return any(a in predefined_allowlist for a in self.allowlist)

class AccessControl(BaseAccessControl):
    def get_accessible_resources(self, resources: List[BaseResource], predefined_allowlist: List[str]) -> List[str]:
        return [res.name for res in resources if res.is_user_allowed(predefined_allowlist)]
