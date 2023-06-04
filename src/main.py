#!/usr/bin/env python3
import sys
import os
import gi
import webbrowser
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Gio, Gdk, Notify


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = Gtk.HeaderBar()  # Move this line up
        self.set_titlebar(self.header)
        # Initialize the notification system
        Notify.init("BeNmap")


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="BeNmap")
        self.win.present()


if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
