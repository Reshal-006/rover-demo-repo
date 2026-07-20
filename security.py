API_KEY = "sk-live-123456789"

def execute(command):
    # Replaced unsafe eval with a safe command mapping
    allowed_commands = {"ping": lambda: "pong", "status": lambda: "ok"}
    if command in allowed_commands:
        return allowed_commands[command]()
    raise ValueError("Invalid command")