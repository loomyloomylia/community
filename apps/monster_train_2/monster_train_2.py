from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.monster_train_2 = r"""
os: windows
and app.exe: /^monstertrain2\.exe$/i
"""

ctx.matches = r"""
os: windows
app: monster_train_2
"""

# @mod.action_class
# class Actions:
