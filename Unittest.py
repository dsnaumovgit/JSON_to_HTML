import unittest
from JSON_to_HTML import JsonToHtml


class TestJsonToHtml(unittest.TestCase):

    def test_parse(self):
        jth.data = [[
            {"title": {"some text": "cosmo"}},
            {"spans": "Title",
            "content":[
                        {"p": "tIT", "span": "44LE", "title": "tITLE", "body": "text676"}
                    ]},
            {"body": "description"},
            {"title": "3456", "body": "text676"},
            {"title": "tITLE", "body": "TEXT"}
        ]]
        self.assertEqual(jth._parse(),
                         "<ul><li><ul><li><title><some text>cosmo</some text></title></li><li><spans>Title</spans>"
                         "<content><ul><li><p>tIT</p><span>44LE</span><title>tITLE</title><body>text676</body></li>"
                         "</ul></content></li><li><body>description</body></li><li><title>3456</title><body>"
                         "text676</body></li><li><title>tITLE</title><body>TEXT</body></li></ul></li></ul>")

if __name__ == "__main__":
    jth = JsonToHtml()
    unittest.main()
