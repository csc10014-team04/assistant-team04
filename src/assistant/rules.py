HELP_MESSAGE = "Available commands: ask for office locations (e.g. 'where is training'), or type 'help' for instructions."  # constant help text

def reply(text: str) -> str:
    text_lower = text.lower()  # normalize input string
    tokens = text_lower.split()  # tokenize query
    if "help" in tokens or text_lower == "help":
        return HELP_MESSAGE  # return command list
    for name, row in offices.items():
        name_lower = name.lower()  # normalize office key
        key_words = [w for w in name_lower.split() if len(w) > 3]  # filter short words
        if name_lower in text_lower or any(w in tokens for w in key_words):
            return f"{row['name']}: room {row['room']}, open {row['hours']}."  # return office info
    return "Sorry, I do not understand. Type 'help' to see available commands."  # default response