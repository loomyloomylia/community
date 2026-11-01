app: libre_office
-
date <number> and <number> and <number>:
    insert("{number_1}/{number_2}/{number_3}")

file export:
    key("ctrl-shift-e")

file save and export:
    key("ctrl-s")
    sleep(0.5)
    key("ctrl-shift-e")
    sleep(0.5)
    edit.left()
    sleep(0.5)
    key("enter")

