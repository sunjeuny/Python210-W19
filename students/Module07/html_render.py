#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

#----------------------------------------#
# Title: html_render.py
# Derived from render.py
# Claire Yoon,2019-02-23,New file
#----------------------------------------#


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

        #  e = P("A paragraph of text", style="text-align: center", id="intro")
        if kwargs is not None:
            self.attributes = {}
            for k, v in kwargs.items():
                self.attributes.update( {k : v})
        else:
            pass


    def append(self, new_content):
        self.contents.append(new_content)

    def ToString(self):
        return str(self.content)

    def _open_tag(self):
        return ("<{}>".format(self.tag))
    def _close_tag(self):
        return ("<{} />".format(self.tag))

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        """<p style="text-align: center" id="intro">
        A paragraph of text
        </p> """
        # out_file.write(self._open_tag())
        # out_file.write("\n")

        for content in self.contents:
            # out_file.write("<{}>\n".format(self.tag))
            open_tag = ["<{}".format(self.tag)]

            if self.attributes is not None:
                for k, v in self.attributes.items():
                    open_tag.append(' ')
                    open_tag.append(k)
                    open_tag.append('=\"')
                    open_tag.append(v)
                    open_tag.append('"')
            open_tag.append(">\n")
            out_file.write("".join(open_tag))

            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))
        # out_file.write(self._close_tag())
        # out_file.write("\n")

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    # def render(self, out_file):
    #     for content in self.contents:
    #         out_file.write("<{}>".format((self.tag)))
    #         try:
    #             content.render(out_file)
    #         except AttributeError:
    #             out_file.write(content)
    #         out_file.write("</{}>\n".format(self.tag))
    # def render(self, out_file):
    #     out_file.write("<{}>".format(self.tag))
    #     out_file.write(self.contents[0])
    #     out_file.write("</{}>\n".format(self.tag))

    # <a href="http://google.com">link</a>
    def render(self, out_file):
        # out_file.write("<{}>".format(self.tag))
        # out_file.write(self.contents[0])
        # # print(self.contents)
        # print(self.contents[0])
        # print(self.attributes)
        # out_file.write("</{}>\n".format(self.tag))

        for content in self.contents:
            open_tag = ["<{}".format(self.tag)]

            if self.attributes is not None:
                for k, v in self.attributes.items():
                    open_tag.append(' ')
                    open_tag.append(k)
                    open_tag.append('=\"')
                    open_tag.append(v)
                    open_tag.append('"')
            open_tag.append(">")
            out_file.write("".join(open_tag))

            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag))


    def append(self, new_content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile):
        open_tag = ["<{}".format(self.tag)]

        if self.attributes is not None:
            for k, v in self.attributes.items():
                open_tag.append(' ')
                open_tag.append(k)
                open_tag.append('=\"')
                open_tag.append(str(v))
                open_tag.append('"')
        open_tag.append(" />\n")
        outfile.write("".join(open_tag))

        # try:
        #     content.render(out_file)
        # except TypeError:
        #     out_file.write(content)
      # outfile.write("\n")
      #   outfile.write("</{}>\n".format(self.tag))
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"


# class A(OneLineTag):
#     def __init__(self, link, content):
#         self.link = link
#         self.content = content

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        # print(kwargs)
        # print(link)
        super().__init__(content, **kwargs)