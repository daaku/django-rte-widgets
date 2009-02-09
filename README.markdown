django-rte-widgets
==================

A collection of editor widgets for use with Django's forms system.


Settings
--------

`RTE_MEDIA_URL` -- For use with bundled assets.


yui
---

Implements a [YUI][1] powered [Rich Text Editor][2]. It uses the [Yahoo!
Hosted][3] copy of YUI assets. The Widget constructor accepts a keyword
argument called `config` which is JSON serialized and passed in to the YUI
Editor constructor. This enable specifying any of the [acceptable configuration
options][4].

### Example:

    widget = YuiTextarea(config={'height': '400px', 'width': '700px', 'format': 'xhtml'})


wmd
---

Implements a [WMD][5] powered [markdown][6] editor. This repository comes
bundled with a copy of the necessary assets (see Settings above). The Widget
constructor accepts a keyword argument called `config` which may contain:

   - *`output`*: The output format, defaults to `Markdown`. Can also be set to
     `HTML`.
   - *`height`*: Defaults to `200px`.
   - *`width`*: Defaults to `700px`.

### Example:

    widget = WmdTextarea(config={'width': '600px'})


  [1]: http://developer.yahoo.com/yui/
  [2]: http://developer.yahoo.com/yui/editor/
  [3]: http://developer.yahoo.com/yui/articles/hosting/
  [4]: http://developer.yahoo.com/yui/docs/YAHOO.widget.Editor.html
  [5]: http://wmd-editor.com/
  [6]: http://daringfireball.net/projects/markdown/syntax
