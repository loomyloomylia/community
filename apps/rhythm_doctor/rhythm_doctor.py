from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.rhythm_doctor = r"""
os: windows
and app.exe: /^rhythm\ doctor\.exe$/i
"""

ctx.matches = r"""
os: windows
app: rhythm_doctor
"""

# @mod.action_class
# class Actions:
