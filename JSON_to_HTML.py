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

    def _parse(self, arg=None):
        arg = arg or self.data
        if isinstance(arg, list):
            return "<ul>{}</ul>".format("".join(["<li>{}</li>".format(self._parse(x)) for x in self.data]))
        result = ""
        for key, value in arg.items():
            result = "{result}<{tag}>{value}</{tag}>".format(result=result, tag=key, value=value)
        return result

    def _save_html(self):
        f = open("index.html", "w")
        f.write(self.row)
        f.close()

    def convert(self):
        self._load_json()
        self.row = self._parse()
        self._save_html()


if __name__ == '__main__':
    data = JsonToHtml()
    data.convert()
