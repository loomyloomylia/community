from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.visual_studio_code = r"""
os: windows
and app.exe: /^code\.exe$/i
"""

ctx.matches = r"""
os: windows
app: visual_studio_code
"""

# @mod.action_class
# class Actions:
