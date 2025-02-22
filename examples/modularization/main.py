#!/usr/bin/env python3
from nicegui import ui

import custom
import home
import pages


# here we use our custom page decorator directly and just put the content creation into a separate function
@custom.page('/', navtitle='Homepage')
def homepage() -> None:
    home.content()


# this call shows that you can also move the whole page creation into a separate file
pages.create()

ui.run()
