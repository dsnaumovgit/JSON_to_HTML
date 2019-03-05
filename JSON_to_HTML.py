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
                if key == 'title':
                    self.row = "{0}<h1>{1}</h1>".format(self.row, value)

                elif key == 'body':
                    self.row = "{row}<p>{value}</p>".format(row=self.row, value=value)
        return self.row

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
