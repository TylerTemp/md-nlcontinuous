#!/usr/bin/python
# coding: utf-8
from markdown import Extension
from markdown.inlinepatterns import Pattern
import re

__version__ = '0.0.1'
__author__ = 'TylerTemp(tylertempdev@gmail.com)'


class NLContinuousPattern(Pattern):
    zh_re = re.compile(
            r'[\u3002\uff1b\uff0c\uff1a\u201c\u201d'
            r'\uff08\uff09\u3001\uff1f\u300a\u300b'
            r'\u4e00-\u9fcc]')

    def handleMatch(self, m):
        prev = m.group(1)
        next = m.group(2)
        zh_re = self.zh_re
        if zh_re.match(prev[-1]) and zh_re.match(next[0]):
            return ''
        return '\n'


class NLContinuous(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('nlctn', NLContinuousPattern(r'\n'), '_begin')


def makeExtension(*args, **kwargs):
    return NLContinuous(*args, **kwargs)


if __name__ == '__main__':
    import markdown
    s = """
中文
中文
English
中文
。
Here

abc
    """

    md = markdown.Markdown(extensions=[makeExtension()])
    print(repr(md.convert(s)))
    print(repr(markdown.Markdown().convert(s)))