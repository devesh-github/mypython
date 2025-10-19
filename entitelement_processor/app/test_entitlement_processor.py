import unittest
from app.entitlement import EntitlementProcessor

class TestEntitlementProcessor(unittest.TestCase):

    def test_basic_allowlist_filtering(self):
        predefined_allowlist = ["Allowed1", "Allowed3"]
        api_response = {
            "userId": "u123",
            "type": "admin",
            "resources": [
                {
                    "user": [
                        {"name": "dashboard", "allowlist": ["Allowed1", "Allowed2"]},
                        {"name": "reports", "allowlist": ["Allowed3"]},
                        {"name": "settings", "allowlist": ["Allowed2"]}
                    ]
                }
            ]
        }

        result = EntitlementProcessor(api_response, predefined_allowlist).build_user_profile()
        print(result.__str__())
        self.assertEqual(result.hasAccess,True)

    def test_no_matching_allowlist(self):
        predefined_allowlist = ["AllowedX"]
        api_response = {
            "userId": "u456",
            "type": "user",
            "resources": [
                {
                    "user": [
                        {"name": "dashboard", "allowlist": ["Allowed1", "Allowed2"]}
                    ]
                }
            ]
        }
        result = EntitlementProcessor(api_response, predefined_allowlist).build_user_profile()
        #print(result.__str__())
        self.assertEqual(result.hasAccess,False)

    def test_empty_resources(self):
        predefined_allowlist = ["Allowed1"]
        api_response = {
            "userId": "u789",
            "type": "guest",
            "resources": []
        }
        from app.entitlement import EntitlementProcessor
        result = EntitlementProcessor(api_response, predefined_allowlist).build_user_profile()
        #print(result.__str__())
        self.assertEqual(result.hasAccess,False)

    def test_missing_allowlist_key(self):
        predefined_allowlist = ["Allowed1"]
        api_response = {
            "userId": "u999",
            "type": "admin",
            "resources": [
                {
                    "user": [
                        {"name": "dashboard"}
                    ]
                }
            ]
        }
        result = EntitlementProcessor(api_response, predefined_allowlist).build_user_profile()
        #print(result.__str__())
        self.assertEqual(result.hasAccess,False)


if __name__ == "__main__":
    unittest.main()
