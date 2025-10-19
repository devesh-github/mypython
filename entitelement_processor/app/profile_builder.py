from abc import ABC, abstractmethod
from typing import List
from models import User

class BaseProfileBuilder(ABC):
    @abstractmethod
    def build_profile(self) -> User:
        pass

class UserProfileBuilder(BaseProfileBuilder):
    def __init__(self, user: User, accessible_resources: List[str]):
        self.user = user
        self.accessible_resources = accessible_resources

    def build_profile(self) -> User:
        self.user.accessibleResources = self.accessible_resources
        self.user.accessCount = len(self.accessible_resources)
        self.user.hasAccess = bool(self.accessible_resources)
        return self.user
