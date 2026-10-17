def reply(text: str) -> str:
    text_lower = text.lower()  # normalize input string
    for name, row in offices.items():
        name_lower = name.lower()  # normalize office key
        key_words = [w for w in name_lower.split() if len(w) > 3]  # filter short words
        if name_lower in text_lower or any(w in text_lower.split() for w in key_words):
            return f"{row['name']}: room {row['room']}, open {row['hours']}."  # return office info
    return "Sorry, I do not understand."  # default response