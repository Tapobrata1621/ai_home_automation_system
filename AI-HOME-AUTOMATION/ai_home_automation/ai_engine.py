# ai_engine.py

def ai_interpret_command(command: str):
    command = command.lower()

    # Simple rule-based AI
    if "turn on" in command and "light" in command:
        return ("light", True)
    if "turn off" in command and "light" in command:
        return ("light", False)

    if "turn on" in command and "fan" in command:
        return ("fan", True)
    if "turn off" in command and "fan" in command:
        return ("fan", False)

    if "turn on" in command and "ac" in command:
        return ("ac", True)
    if "turn off" in command and "ac" in command:
        return ("ac", False)

    if "open" in command and "door" in command:
        return ("door", True)
    if "close" in command and "door" in command:
        return ("door", False)

    return (None, None)
