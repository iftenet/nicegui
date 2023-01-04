def remove_prefix(text: str, prefix: str) -> str:
    return text[len(prefix):] if prefix and text.startswith(prefix) else text
