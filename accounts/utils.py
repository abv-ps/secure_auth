from django.utils.html import escape


def safe_output(text: str) -> str:
    return escape(text)
