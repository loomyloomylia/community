from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.endless_legend_2 = r"""
os: windows
and app.exe: /^endless\ legend\ 2\.exe$/i
"""

ctx.matches = r"""
os: windows
app: endless_legend_2
"""

# @mod.action_class
# class Actions:
