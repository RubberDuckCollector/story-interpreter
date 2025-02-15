# Table of contents

<!-- vim-markdown-toc GFM -->

* [Story interpreter](#story-interpreter)
* [Story format](#story-format)
* [Tags](#tags)
* [Prerequisites](#prerequisites)
* [Disclaimer](#disclaimer)
* [TODO](#todo)

<!-- vim-markdown-toc -->

# Story interpreter

https://docs.python.org/3/library/html.parser.html

**idea: a program that can interpret a story with timing
markers to print text at different speeds as specified in the story,
allowing the writer to illustrate elements of the story through the timing
of when and how fast words and letters appear on the screen**

# Story format

- uses HTML parser

`<speed, value=10>Hello world</speed>`

# Tags

- [x] `<speed val=n>DATA</speed> (types the data within the tags at a rate of n speed in seconds)`
- [ ] `<pause val=n> (pause typing for n seconds)`
- [ ] `<alternate val=n>E</alternate> (deletes and re-types a character/data at a rate of n speed in seconds, but would work best with single characters)`

# Prerequisites

- The program comes with example stories but also works from `.html` files.

# Disclaimer

**Program will not output correctly if the text is not inside valid tags.
e.g: misspelled "color" tags won't activate color correctly and misspellt "speed" tags won't allow the text to be outputted.**

# TODO

- [ ] implement argparse
- [x] figure out new lines (`<br>`?)
- [x] implement styles
- [x] figure out how to injest a file
- [x] implement colours
