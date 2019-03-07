import unittest
from JSON_to_HTML import JsonToHtml


class TestJsonToHtml(unittest.TestCase):

    def test_parse(self):
        jth.data = {
            "title.body.span.text#id-read": {"some text": "cosmo"},
            "spans": "Title",
            "content.class_name.fig": {"p": "tIT", "span": "44LE", "title": "tITLE", "body": "text676"},
            "body#id_head": {"title": "3456", "body": "text676"}
        }
        self.assertEqual(jth._parse(),
                         '<title id="id-read" class="body span text"><some>cosmo</some></title><spans>Title</spans>'
                         '<content class="class_name fig"><p>tIT</p><span>44LE</span><title>tITLE</title><body>'
                         'text676</body></content><body id="id_head"><title>3456</title><body>text676</body></body>')

if __name__ == "__main__":
    jth = JsonToHtml()
    unittest.main()
