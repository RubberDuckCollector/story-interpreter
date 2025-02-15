# Table of contents

<!-- vim-markdown-toc GFM -->

* [Story interpreter](#story-interpreter)
* [Story format](#story-format)
* [Tags](#tags)
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

```HTML
- [x] <speed val=n>DATA</speed> (types the data within the tags at a rate of n speed in seconds)
- [ ] <pause val=n> (pause typing for n seconds)
- [ ] <alternate val=n>E</alternate> (deletes and re-types a character/data at a rate of n speed in seconds, but would work best with single characters)
```

# TODO

- [ ] figure out new lines (`<br>`?)
- [ ] figure out how to injest a file
- [ ] implement argparse
