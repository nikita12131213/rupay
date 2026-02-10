import io
import unittest
from contextlib import redirect_stdout

from ru_python.translator import translate_code


class RunTests(unittest.TestCase):
    def test_exec_translated_code(self) -> None:
        source = """
функция привет():
    печать("ок")

привет()
"""
        python_code = translate_code(source)
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(python_code, "<test>", "exec"), {})
        self.assertEqual(output.getvalue().strip(), "ок")


if __name__ == "__main__":
    unittest.main()
