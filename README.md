sublime-qtdoc
=============

A Qt documentation helper for Sublime Text 2 that opens the Qt API documentation for a given class in the default browser.


Installation
------------
To install this plugin, copy the `QtDoc` folder to your Sublime Text 2 `Packages` directory.

Usage
-----
The helper is called by using the keyboard shortcut `Ctrl+Shift+h` or `Cmd+Shift+h`, depending on your operating system. If you have a selection, the helper will try to use your selection as a Qt class name. Multiple selections will all be processed. Selections that span multiple lines will be split and each line will be processed.

If you have no selection, the helper will use the word that your cursor is currently on or next to as the Qt class name.
