#!/usr/bin/python
# coding: utf-8

import unittest
import itertools
import markdown
import nlcontinuous


class Test(unittest.TestCase):

    zh = '中。；，：“”（）、？《》'
    en = 'e()[]{}.,?/\\<>|+_=-~!@#$%^&* '

    def setUp(self):
        self.m = markdown.Markdown(extensions=[nlcontinuous.makeExtension()])
        self.zh_zh = itertools.permutations(self.zh, 2)
        self.en_en = itertools.permutations(self.en, 2)
        self.zh_en = itertools.product(self.zh, self.en)
        self.en_zh = itertools.product(self.en, self.zh)

    def eq(self, source, expect):
        target = self.m.convert(source)
        self.assertEqual(target, expect)

    def test_zh_zh(self):
        for sep in ('\n', '\r\n'):
            for each in self.zh_zh:
                source = sep.join(each)
                self.eq(source, '<p>%s%s</p>' % each)

    def test_en_en(self):
        for sep in ('\n', '\r\n'):
            for each in self.en_en:
                source = sep.join(each)
                if source[-1] in '>#=- ':
                    continue
                if source[0] in '># ':
                    continue
                expect = '<p>%s\n%s</p>' % tuple(self.es(x) for x in each)
                self.eq(source, expect)

    def test_zh_en(self):
        for sep in ('\n', '\r\n'):
            for each in self.zh_en:
                source = sep.join(each)
                if source[-1] in '>#=- ':
                    continue
                expect = '<p>%s\n%s</p>' % (each[0], self.es(each[1]))
                self.eq(source, expect)

    def test_en_zh(self):
        for sep in ('\n', '\r\n'):
            for each in self.en_zh:
                source = sep.join(each)
                if source[0] in '># ':
                    continue
                expect = '<p>%s\n%s</p>' % (self.es(each[0]), each[1])
                self.eq(source, expect)

    def es(self, s):
        return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

if __name__ == '__main__':
    unittest.main()