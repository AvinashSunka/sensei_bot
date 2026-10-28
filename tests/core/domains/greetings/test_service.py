from src.core.domains.greetings.service import GreetingsService

def test_generate_welcome_message():
    service = GreetingsService()
    result = service.generate_welcome_message(username="@User", server_name="MyServer")
    
    assert result == "Welcome to MyServer, @User! Please read the rules."
    assert "@User" in result

def test_generate_hello_response():
    service = GreetingsService()
    result = service.generate_hello_response(username="@Bob")
    
    assert result == "Hello there, @Bob!"