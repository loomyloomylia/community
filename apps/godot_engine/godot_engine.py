from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.godot_engine = r"""
os: windows
and app.exe: /^backpackbattles\.exe$/i
"""

ctx.matches = r"""
os: windows
app: godot_engine
"""

# @mod.action_class
# class Actions:
