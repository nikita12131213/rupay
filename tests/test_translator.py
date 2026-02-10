import unittest

from ru_python.translator import KEYWORD_MAP, translate_code


class TranslatorTests(unittest.TestCase):
    def test_does_not_translate_strings_or_comments(self) -> None:
        source = 'печать("если")  # если\n'
        translated = translate_code(source)
        self.assertIn('print("если")', translated)
        self.assertIn('# если', translated)

    def test_translates_keywords(self) -> None:
        source = """
если Истина:
    печать(длина("abc"))
"""
        translated = translate_code(source)
        self.assertIn("if True:", translated)
        self.assertIn("print(len(\"abc\"))", translated)

    def test_all_keywords_have_mapping(self) -> None:
        for key, value in KEYWORD_MAP.items():
            translated = translate_code(key)
            self.assertEqual(translated, value)


if __name__ == "__main__":
    unittest.main()
