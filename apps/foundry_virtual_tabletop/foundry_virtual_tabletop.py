from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.foundry_virtual_tabletop = r"""
os: windows
and app.exe: /^foundry\ virtual\ tabletop\.exe$/i
"""

ctx.matches = r"""
os: windows
app: foundry_virtual_tabletop
"""

# @mod.action_class
# class Actions:
