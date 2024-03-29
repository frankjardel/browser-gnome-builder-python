# window.py
#
# Copyright 2022 jardel
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.
#
# SPDX-License-Identifier: MIT
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("WebKit2", "5.0")

from gi.repository import Gtk, WebKit2

@Gtk.Template(resource_path='/dev/up7/browser/window.ui')
class BrowserWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BrowserWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.web_view = WebKit2.WebView()
        self.web_view.load_uri("https://www.gnome.org/")
        self.set_child(self.web_view)


    @Gtk.Template.Callback()
    def on_uri_entry_activated(self, entry):
        uri = entry.get_text()
        self.web_view.load_uri(uri)


