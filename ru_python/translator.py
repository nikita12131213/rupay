"""Переводчик русского синтаксиса в стандартный Python."""

from __future__ import annotations

import io
import tokenize
from typing import Dict

KEYWORD_MAP: Dict[str, str] = {
    "если": "if",
    "иначе": "else",
    "иначеесли": "elif",
    "для": "for",
    "пока": "while",
    "функция": "def",
    "класс": "class",
    "вернуть": "return",
    "прервать": "break",
    "продолжить": "continue",
    "попытаться": "try",
    "кроме": "except",
    "наконец": "finally",
    "поднять": "raise",
    "передать": "pass",
    "утверждать": "assert",
    "импорт": "import",
    "из": "from",
    "как": "as",
    "Истина": "True",
    "Ложь": "False",
    "Ничего": "None",
    "печать": "print",
    "ввод": "input",
    "длина": "len",
    "диапазон": "range",
    "целое": "int",
    "число": "float",
    "строка": "str",
    "список": "list",
    "словарь": "dict",
    "множество": "set",
    "кортеж": "tuple",
    "открыть": "open",
}


def translate_code(source: str) -> str:
    """Переводит исходный код на .rupy в валидный Python.

    Переводятся только токены типа NAME, совпадающие со словарём KEYWORD_MAP.
    Строки и комментарии остаются без изменений.
    """
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    translated = []
    for token in tokens:
        if token.type == tokenize.NAME and token.string in KEYWORD_MAP:
            token = tokenize.TokenInfo(
                token.type,
                KEYWORD_MAP[token.string],
                token.start,
                token.end,
                token.line,
            )
        translated.append(token)
    return tokenize.untokenize(translated)
