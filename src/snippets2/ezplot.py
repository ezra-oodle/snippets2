#!/usr/bin/env python3
import plotnine as p9

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
    

def oodle_watermark(filename= 'img/Oodle Car Finance Logo (digital).png',*args,**kwargs):
    return p9.watermark(filename,*args,**kwargs)

