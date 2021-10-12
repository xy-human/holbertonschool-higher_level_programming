#!/usr/bin/python3
"""Validate inherence"""
def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False