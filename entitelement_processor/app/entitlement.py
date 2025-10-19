from typing import Dict, List
from access_control import AccessControl, Resource
from profile_builder import UserProfileBuilder
from models import User

class EntitlementProcessor:
    def __init__(self, api_response: Dict, predefined_allowlist: List[str]):
        self.api_response = api_response
        self.predefined_allowlist = predefined_allowlist
        self.user = User(api_response["userId"], api_response["type"])
        self.resources = self.parse_resources(api_response.get("resources", []))
        self.access_control = AccessControl()

    def parse_resources(self, resource_data: List[Dict]) -> List[Resource]:
        resources: List[Resource] = []
        for resource_entry in resource_data:
            for _, resource_list in resource_entry.items():
                for r in resource_list:
                    resources.append(Resource(r.get("name"), r.get("allowlist", [])))
        return resources

    def build_user_profile(self) -> User:
        accessible = self.access_control.get_accessible_resources(self.resources, self.predefined_allowlist)
        builder = UserProfileBuilder(self.user, accessible)
        return builder.build_profile()
