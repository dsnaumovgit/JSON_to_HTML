import json


class JsonToHtml:

    def __init__(self, file=None):
        self.data = None
        self.file = file or 'source.json'
        self.row = ""

    # load json file
    def _load_json(self):
        f = open(self.file)
        self.data = json.load(f)
        f.close()

    # parse list by element
    def _parse_list(self, arg):
        return "<ul>{}</ul>".format("".join(["<li>{}</li>".format(self._parse(x)) for x in arg]))

    # parse dict by element
    def _parse_dict(self, arg):
        result = ""
        for key, value in arg.items():
            result = "{result}<{tag}>{value}</{tag}>".format(result=result, tag=key, value=self._parse(value))
        return result

    def _parse(self, arg=None):
        """
        The parse function converts a file in a json file into an html file.
        As an optional parameter takes a string in a json format (default parameter: self.data).
        Returns a string in html format.
            >>> self._parse('[{"TAG": "description"}]')
            return: "<ul><li><TAG>description</TAG></li></ul>"
        """

        arg = arg or self.data
        if isinstance(arg, list):
            return self._parse_list(arg)

        elif isinstance(arg, dict):
            return self._parse_dict(arg)

        else:
            return arg

    # save to html file
    def _save_html(self):
        f = open("index.html", "w")
        f.write(self.row)
        f.close()

    def convert(self):
        """
        Function - user interface.
        Convert source.json file to index.html file
            >>> obj.convert()
        """

        self._load_json()
        self.row = self._parse()
        self._save_html()


if __name__ == '__main__':
    data = JsonToHtml()
    data.convert()
