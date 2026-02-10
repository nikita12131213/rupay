"""CLI для запуска .rupy файлов и REPL."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .repl import start_repl
from .translator import translate_code


def _run_code(source: str, filename: str, show_python: bool) -> int:
    python_code = translate_code(source)
    if show_python:
        print("--- Сгенерированный Python ---")
        print(python_code)
        print("--- Конец ---")
    try:
        code_obj = compile(python_code, filename, "exec")
    except SyntaxError as exc:
        print(f"Синтаксическая ошибка: {exc}", file=sys.stderr)
        return 1
    exec(code_obj, {})
    return 0


def _run_file(path: Path, show_python: bool) -> int:
    if not path.exists():
        print(f"Файл не найден: {path}", file=sys.stderr)
        return 1
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Не удалось прочитать файл: {exc}", file=sys.stderr)
        return 1
    return _run_code(source, str(path), show_python)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rupy",
        description="Русский синтаксис поверх Python через препроцессор",
    )
    parser.add_argument(
        "-c",
        dest="command",
        help="Выполнить однострочный код",
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    run_parser = subparsers.add_parser("run", help="Выполнить .rupy файл")
    run_parser.add_argument("path", type=str, help="Путь к .rupy файлу")
    run_parser.add_argument(
        "--show-python",
        action="store_true",
        help="Показать сгенерированный Python-код",
    )

    subparsers.add_parser("repl", help="Интерактивная оболочка")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is not None:
        sys.exit(_run_code(args.command, "<команда>", show_python=False))

    if args.subcommand == "run":
        sys.exit(_run_file(Path(args.path), show_python=args.show_python))

    if args.subcommand == "repl":
        start_repl()
        return

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
