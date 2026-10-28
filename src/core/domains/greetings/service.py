class GreetingsService:
    """Handles the business logic for all greeting behaviors."""
    
    def generate_welcome_message(self, username: str, server_name: str) -> str:
        return f"Welcome to {server_name}, {username}! Please read the rules."

    def generate_hello_response(self, username: str) -> str:
        return f"Hello there, {username}!"