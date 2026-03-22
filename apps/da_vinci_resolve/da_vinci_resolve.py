from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.da_vinci_resolve = r"""
os: windows
and app.exe: /^resolve\.exe$/i
"""

ctx.matches = r"""
os: windows
app: da_vinci_resolve
"""

# @mod.action_class
# class Actions:
