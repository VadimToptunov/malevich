import datetime

import termcolor
from PIL import Image
import random
import string
import pathlib
from datetime import date

min = 0
col_max = 256
name_length = 16


def create_image(width, height):
    r = lambda: random.randint(0, 255)
    im = Image.new("RGB", (width, height), '#{:02x}{:02x}{:02x}'.format(r(), r(), r()))
    for i in range(random_int(min, height)):
        for j in range(random_int(min, height)):
            im.paste((random_color()), (random_int(min, width), random_int(min, height), random_int(min, width),
                                        random_int(min, height)))
        im.save(create_random_filename())


def random_int(min, max):
    return random.randint(min, max)


def random_color():
    return random.randint(min, col_max), random.randint(min, col_max), random.randint(min, col_max)


def create_random_filename():
    directory = f"../masterpieces/{date.today()}/{datetime.datetime.now().time().hour}/"
    filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length)) + ".jpg"
    if not pathlib.Path(directory).exists():
        pathlib.Path(directory).mkdir(parents=True)
    else:
        pass
    filepath = f"{directory}{filename}"
    text = f"File: {filepath}"
    print(termcolor.colored(text, "green"))
    return filepath
