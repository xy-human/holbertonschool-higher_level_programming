#!/usr/bin/python3
"""Function init_line_blank called by text_indentation()
    rerun string in find of spaces"""


def init_line_blank(string, position):
    """Args: string, position
        return position modified"""
    if len(string) > position:
        while string[position] == ' ':
            position += 1
    return position

"""Function text_indentation print a string with conditionals"""


def text_indentation(text):
    """Args: text
        without return"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    i = init_line_blank(text, i)
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in (".:?"):
            print("\n")
            i = init_line_blank(text, i + 1)
        else:
            i += 1
