# This is a file to place themes
# Would've place it in json file, however due to the difficulties of the limitation that it does not support any math operation
# Python file is used instead
# Besides, we can put some methods here
from typing import Optional

def rgba(r: int, g: int, b: int, a: Optional[int] = 1):
    """

    :param r: The color red (0,255)
    :param g: The color green (0,255)
    :param b: The color blue (0,255)
    :param a: The Alpha or visibility of the color (0-1)
    :return: the color in 0 and 1 range
    """
    return r/255, g/255, b/255, a

theme_list = ['dark','light']

themes = {
    'dark':{
        'background_color': rgba(40,40,40),
        'button_color': rgba(69,69,69),
        'text_color': rgba(220,220,220),
        'border_color':rgba(0,0,0)
    },

    'light':{
        'background_color': rgba(225,225,225),
        'button_color': rgba(230,230,230),
        'text_color': rgba(25,25,25),
        'border_color':rgba(77, 210, 255)
    }
}
