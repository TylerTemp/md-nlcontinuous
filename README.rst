.. md-nlcontinuous
.. README.rst

md-nlcontinuous
===============

Python Markdown extension which prevents white space after line break in Chinese

Install
-------

.. code:: bash

    pip install git+git://github.com/TylerTemp/md-nlcontinuous.git


Usage
-----

.. code:: python

    import markdown
    import nlcontinuous
    s = '中文\n中文'
    print(markdown.markdown(s, extensions=[nlcontinuous.makeExtension()])
    # <p>中文中文</p>

By default markdown will keep the line breaker (`\n`), which is not neccessary
in Chinese.

`nlcontinuous` will remove that space, but keep it when it's not Chinese.

.. code:: python

    >>> s = '中文\n中文'
    >>> markdown.markdown(s)
    <p>中文\n中文</p>
    >>> markdown.markdown(s, extensions=[nlcontinuous.makeExtension()])
    <p>中文中文</p>
    >>> markdown.markdown('中文\nEnglish', extensions=[nlcontinuous.makeExtension()])
    <p>中文\nEnglish</p>
    >>> markdown.markdown('嗯。\n就酱', extensions=[nlcontinuous.makeExtension()])  # zh-punctuation
    <p>嗯。就酱</p>
