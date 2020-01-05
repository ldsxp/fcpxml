from pprint import pprint as pp

import xml.etree.ElementTree as ET

from .utils import _generate_fields

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


class VideoFormat:
    def __init__(self, element=None):
        self.samplecharacteristics = None
        self.fields = ['samplecharacteristics', ]
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'samplecharacteristics':
                # self.samplecharacteristics = VideoSampleCharacTeristics(element_child)
                print('我们先不处理格式信息 VideoSampleCharacTeristics')
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class VideoClipItem:
    def __init__(self, element=None):
        self.masterclipid = None
        self.name = None
        self.enabled = None
        self.duration = None
        self.rate = None
        self.start = None
        self.end = None
        self.in_ = None
        self.out = None
        self.pproTicksIn = None
        self.pproTicksOut = None
        self.alphatype = None
        self.pixelaspectratio = None
        self.anamorphic = None
        self.file = None
        self.logginginfo = None
        self.colorinfo = None
        self.labels = None
        self.links = []
        self.fields = ['masterclipid', 'name', 'enabled', 'duration', 'rate', 'start', 'end', 'in', 'out',
                       'pproTicksIn', 'pproTicksOut', 'alphatype', 'pixelaspectratio', 'anamorphic', 'file', 'links',
                       'logginginfo', 'colorinfo', 'labels']

        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'masterclipid':
                self.masterclipid = element_child.text
            elif element_child.tag == 'name':
                self.name = element_child.text
            elif element_child.tag == 'enabled':
                self.enabled = element_child.text
            elif element_child.tag == 'duration':
                self.duration = element_child.text
            elif element_child.tag == 'rate':
                self.rate = Rate(element_child)
            elif element_child.tag == 'start':
                self.start = element_child.text
            elif element_child.tag == 'end':
                self.end = element_child.text
            elif element_child.tag == 'in':
                self.in_ = element_child.text
            elif element_child.tag == 'out':
                self.out = element_child.text
            elif element_child.tag == 'pproTicksIn':
                self.pproTicksIn = element_child.text
            elif element_child.tag == 'pproTicksOut':
                self.pproTicksOut = element_child.text
            elif element_child.tag == 'alphatype':
                self.alphatype = element_child.text
            elif element_child.tag == 'pixelaspectratio':
                self.pixelaspectratio = element_child.text
            elif element_child.tag == 'anamorphic':
                self.anamorphic = element_child.text
            elif element_child.tag == 'file':
                # self.file = element_child.text
                print('需要处理 file')
            elif element_child.tag == 'logginginfo':
                # self.logginginfo = element_child.text
                print('需要处理 logginginfo')
            elif element_child.tag == 'colorinfo':
                # self.colorinfo = element_child.text
                print('需要处理 colorinfo')
            elif element_child.tag == 'labels':
                self.labels = element_child.text
            elif element_child.tag == 'link':
                for link in element_child:
                    self.links.append(link)
                print('需要处理 link')
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class VideoTrack:
    def __init__(self, element=None):
        self.clipitems = []
        self.enabled = None
        self.locked = None
        self.fields = ['clipitem', 'enabled', 'locked']
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'clipitem':
                self.clipitems.append(VideoClipItem(element_child))
            elif element_child.tag == 'enabled':
                self.enabled = element_child.text
            elif element_child.tag == 'locked':
                self.locked = element_child.text
            else:
                print(f'未知内容({type(self).__name__}):{element_child} 标签:{element_child.tag} {type(element_child)}',
                      element_child.text)

    def __str__(self):
        return type(self).__name__ + " ,".join([f"({f}: {getattr(self, f, None)})" for f in self.fields])

    def __repr__(self):
        return self.__str__()


class Video:
    def __init__(self, element=None):
        self.format = None
        self.tracks = []
        self.fields = ['format', 'tracks', ]
        if element is not None:
            self.parser(element)

    def parser(self, element):
        for element_child in element:
            if element_child.tag == 'format':
                self.format = VideoFormat(element_child)
            elif element_child.tag == 'track':
                self.tracks.append(VideoTrack(element_child))
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
                self.video = Video(element_child)
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
