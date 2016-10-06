=============
Marked format
=============

The *Marked* format is a generic lightweight meta-format to structure documents.
It is inspired on Markdown (although it is not necessarily compatible). From
the base *Marked* format, we derive many other similar formats to represent
specific document types (Markio, Formarked, etc).

Once the basic *Marked* format is defined, it is easy to derive new formats and
parsers to specific applications. This section describes the basic format.

All *Marked* files consist of 4 parts that must appear in the following order:
a title, some meta information, a short description and a list of sections.
The example shows it::

    Document title
    ==============

        Meta-1: value 1
        Meta-2: value 2

    A short description paragraph.

    Section 1
    ---------

    Section contents.

    Section 2 (tag 1, tag 2)
    ------------------------

    More contents...

The title is the only required part. It can be followed by an indented
section with meta-information with ``key: value`` pairs (that is actually YAML,
but more on that later). Following the "meta" section is a paragraph with some
textual description. It comprises any piece of text between the end of the
meta section and the first section title.

Finally, the document can have any number of sections separated by their
respective titles. Each title can be tagged (the contents inside parenthesis),
and these tags can be used to retrieve specific versions of the given section.

A string of *Marked* data can be parsed with the ``parse_marked()`` function.
The resulting object is an :class:`markio.Marked` instance that expose each part
of the document in the corresponding attribute:

.. code-block:: python
    :hidden:

    from markio import parse_marked

    data = """
    Document title
    ==============

        Meta-1: value 1
        Meta-2: value 2

    A short description paragraph.

    Section 1
    ---------

    Section contents.

    Section 2 (tag 1, tag 2)
    ------------------------

    More contents...
    """

>>> marked = parse_marked(data)
>>> marked.title
'Document title'
>>> marked.meta['Meta-1']
'value 1'
>>> marked.short_description
'A short description paragraph.'
>>> marked.sections[0]
Section('Section 1', 'Section contents.')

The rest of this document explores each of these sections in greater detail.


Title
=====

A string with the document title. It can be accessed by the ``.title`` attribute
in the Marked object. Not much to talk here ;-)


Meta
====

The *meta* section consists in an indented YAML document formed by key: value
pairs.