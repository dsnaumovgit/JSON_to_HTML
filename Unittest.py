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
                         "<h1>some text</h1><p>description</p><h1>3456</h1><p>text676</p><h1>tITLE</h1><p>TEXT</p>")

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
