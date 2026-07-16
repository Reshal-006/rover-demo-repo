API_KEY = "sk-live-123456789"

def execute(command):
    # BUG 5: Unsafe eval
    return eval(command)