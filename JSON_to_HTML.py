import re
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

    def _parse_tag(self, arg, **kwargs):
        # find to the point (tag name)
        tag = re.match('\w+', arg).group(0)
        if kwargs['where'] == 'end':
            return tag

        # find to the end of the line or '#' (class name)
        regex = re.compile('(?<=%s\.)[^#]+'%tag)
        class_find = re.findall(regex, arg)
        class_value = ""
        if len(class_find) > 0:
            class_replace = class_find[0].replace('.', ' ')
            class_value = ' class="{}"'.format(class_replace)

        # find id if it is
        id_value = re.findall('(?<=#).+', arg)
        id_str = ""
        if id_value:
            id_str = ' id="{id}"'.format(id=id_value[0])

        return '{tag}{id}{class_value}'.format(tag=tag, id=id_str, class_value=class_value)

    # parse list by element
    # def _parse_list(self, arg):
    #     return "<ul>{}</ul>".format("".join(["<li>{}</li>".format(self._parse(x)) for x in arg]))

    # parse dict by element
    def _parse_dict(self, arg):
        result = ""
        for key, value in arg.items():
            result = "{result}<{tag_start}>{value}</{tag_end}>".format(result=result,
                                                                       tag_start=self._parse_tag(key, where='start'),
                                                                       tag_end=self._parse_tag(key, where='end'),
                                                                       value=self._parse(value))
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
        if isinstance(arg, dict):
            return self._parse_dict(arg)

        else:
            if ("<" and ">") in arg:
                arg = arg.replace("<", "&lt;").replace(">", "&gt;")
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
