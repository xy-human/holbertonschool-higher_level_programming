#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    stderr_fileno = sys.stderr
    validate = True
    try:
        result = fct(args[0], args[1])
    except Exception as ex:
        stderr_fileno.write("Exception: {}\n".format(ex))
        validate = False
    return result if validate else None
