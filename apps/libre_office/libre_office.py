from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.libre_office = r"""
os: windows
and app.exe: /^soffice\.bin$/i
"""

ctx.matches = r"""
os: windows
app: libre_office
"""

# @mod.action_class
# class Actions:
