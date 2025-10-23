from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.libre_wolf = r"""
os: windows
and app.exe: /^librewolf\.exe$/i
"""

ctx.matches = r"""
os: windows
app: libre_wolf
"""

# @mod.action_class
# class Actions:
