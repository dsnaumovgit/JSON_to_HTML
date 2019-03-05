import json


class JsonToHtml:

    def __init__(self, file=None):
        self.data = None
        self.file = file or 'source.json'
        self.row = ""

    def _load_json(self):
        f = open(self.file)
        self.data = json.load(f)
        f.close()

    def _parse(self):
        for elem in self.data:
            for key, value in elem.items():
                self.row = "{row}<{tag}>{value}</{tag}>".format(row=self.row, tag=key, value=value)

    def _save_html(self):
        f = open("index.html", "w")
        f.write(self.row)
        f.close()

    def convert(self):
        self._load_json()
        self._parse()
        self._save_html()


if __name__ == '__main__':
    data = JsonToHtml()
    data.convert()
