from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.slay_the_spire_2 = r"""
os: windows
and app.exe: /^slaythespire2\.exe$/i
"""

ctx.matches = r"""
os: windows
app: slay_the_spire_2
"""

# @mod.action_class
# class Actions:
