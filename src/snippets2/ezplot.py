#!/usr/bin/env python3
import plotnine as pn

class Colours:
    """A dataclass for Oodle's color pallete"""
    
    # Primary Palette
    oodle_teal = '#0AD2A0'
    oodle_navy = '#312F43'
    oodle_white = '#FFFFFF'

    # Secondary Palette
    oodle_pink = '#EC608A'
    oodle_orange = '#FB9F1E'
    oodle_purple = '#6059A3'


    def __init__(self):
        pass
    
import pkg_resources

def oodle_watermark(*args,**kwargs):
    FILE_PATH = pkg_resources.resource_filename('snippets2','img/oodle_logo.png')
    return pn.watermark(FILE_PATH,*args,**kwargs)

