from typing import List

class User:
    def __init__(self, user_id: str, user_type: str, accessibleResources: List[str] = None,
                 accessCount: int = 0, hasAccess: bool = False):
        self.user_id = user_id
        self.user_type = user_type
        self.accessibleResources = accessibleResources or []
        self.accessCount = accessCount
        self.hasAccess = hasAccess

    def __str__(self):
        return (f"User(user_id={self.user_id}, user_type={self.user_type}, "
                f"accessibleResources={self.accessibleResources}, "
                f"accessCount={self.accessCount}, hasAccess={self.hasAccess})")