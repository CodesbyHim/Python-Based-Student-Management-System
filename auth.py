## `auth.py`

from database import DatabaseManager

class AuthManager:
    def __init__(self):
        self.db = DatabaseManager()
        self.db.add_user("admin", "admin")  # Default credentials

    def login(self, username, password):
        return self.db.validate_user(username, password)