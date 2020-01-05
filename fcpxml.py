import xml.etree.ElementTree as ET

media_tree = ['video', 'audio', ]


class Rate:
    def __init__(self, element=None):
        self.timebase = None
        self.ntsc = None
        self.fields = ['timebase', 'ntsc', ]
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'timebase':  # text
                self.timebase = element_child.text
            elif element_child.tag == 'ntsc':  # text
                self.ntsc = element_child.text
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class Timecode:
    def __init__(self, element=None):
        self.string = None
        self.frame = None
        self.displayformat = None
        self.rate = None
        self.fields = ['string', 'frame', 'displayformat', 'rate', ]
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'string':  # text
                self.string = element_child.text
            elif element_child.tag == 'frame':  # text
                self.frame = element_child.text
            elif element_child.tag == 'displayformat':  # text
                self.displayformat = element_child.text
            elif element_child.tag == 'rate':
                self.rate = Rate(element_child)
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class Media:
    def __init__(self, element=None):
        self.string = None
        self.video = None
        self.audio = None
        self.fields = ['video', 'audio', ]
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'video':
                self.video = element_child
            elif element_child.tag == 'audio':
                self.audio = element_child
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class Sequence:
    def __init__(self, element=None):
        self.uuid = None
        self.name = None
        self.duration = None
        self.fields = ['uuid', 'duration', 'name', 'rate', 'timecode', 'media', ]
        self.fields_tree = ['labels', ]
        self.rate = None
        self.timecode = None
        self.media = None
        self.attrib = {}
        if element is not None:
            self.parser(element)

    def parser(self, element):
        self.attrib = element.attrib
        for element_child in element:
            if element_child.tag == 'uuid':  # text
                self.uuid = element_child.text
            elif element_child.tag == 'duration':  # text
                self.duration = element_child.text
            elif element_child.tag == 'name':  # text
                self.name = element_child.text
            elif element_child.tag == 'rate':  # tree
                self.rate = Rate(element_child)
            elif element_child.tag == 'media':  # tree
                self.media = Media(element_child)
            elif element_child.tag == 'timecode':  # tree
                self.timecode = Timecode(element_child)
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class FCPXML:
    """
    Final Cut Pro 7 XML
    不支持 Final Cut Pro X XML
    """

    def __init__(self, xml_file):
        # 从文件中读取数据
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.sequence_list = []
        self.parser(self.root)

    def parser(self, root):
        # element
        # 可以迭代子节点
        for sequence in root:
            print(f'标签:{root.tag}, 文本:{root.text}\n属性字典 {"-" * 70}')
            # pp(sequence.attrib)
            self.sequence_list.append(Sequence(sequence))
