import re
import sublime_plugin
import webbrowser


class QtdocCommand(sublime_plugin.TextCommand):
    """ A sublime command to open the documentation for the selected text,
    which is assumed to be the name of a Qt class.

    """
    def run(self, edit):
        qpattern = r'^Q[a-zA-z]+$'
        klass = ''
        # Attempt to split the selection into lines (assumes each line is a
        # Qt class)
        self.view.run_command('split_selection_into_lines')
        for region in self.view.sel():
            if region.empty():
                # Look for Qt classes around the cursor.
                klass = self.view.substr(self.view.word(region))
            else:
                # Look within the selection.
                klass = self.view.substr(region)

            if re.match(qpattern, klass):
                url = "http://qt-project.org/doc/qt-4.8/{0}.html"
                webbrowser.open(url.format(klass.strip().lower()))
