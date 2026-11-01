mode: command
mode: dictation
-
# ^dictation mode$:
#     mode.disable("sleep")
#     mode.disable("command")
#     mode.enable("dictation")
#     user.code_clear_language_mode()
#     user.gdb_disable()
# ^command mode$:
#     mode.disable("sleep")
#     mode.disable("dictation")
#     mode.enable("command")
#     user.command_mode_color_preset()

^dictation mode$: user.dictation_mode()
^command mode$: user.command_mode()
^mixed mode$: user.mixed_mode()
