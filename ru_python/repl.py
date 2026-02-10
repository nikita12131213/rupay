"""Простой REPL для русского синтаксиса."""

from __future__ import annotations

import sys

from .translator import translate_code


def start_repl() -> None:
    print("Русский Python REPL. Введите 'выход' для завершения.")
    globals_dict: dict[str, object] = {}
    while True:
        try:
            line = input("rupy> ")
        except EOFError:
            print()
            break

        if not line.strip():
            continue
        if line.strip() in {"выход", "exit"}:
            break

        try:
            python_code = translate_code(line)
            code_obj = compile(python_code, "<repl>", "exec")
            exec(code_obj, globals_dict)
        except SyntaxError as exc:
            print(f"Синтаксическая ошибка: {exc}", file=sys.stderr)
        except Exception as exc:
            print(f"Ошибка выполнения: {exc}", file=sys.stderr)
