import unittest
from JSON_to_HTML import JsonToHtml


class TestJsonToHtml(unittest.TestCase):

    def test_parse(self):
        jth.data = [
            {"title": "some text", "body": "description"},
            {"title": "3456", "body": "text676"},
            {"title": "tITLE", "body": "TEXT"}
        ]
        jth._parse()
        self.assertEqual(jth.row,
                         "<title>some text</title><title>some text</title><body>description</body><title>3456</title>"
                         "<body>text676</body><title>tITLE</title><body>TEXT</body>")

    def test_non_parse(self):
        jth.data = [
            {"title": "some text"},
            ["TEXT"]
        ]
        with self.assertRaises(AttributeError):
            jth._parse()


if __name__ == "__main__":
    jth = JsonToHtml()
    unittest.main()
