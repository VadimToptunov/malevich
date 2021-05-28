from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
import random
import Tech

color_scheme = "RGB"
min = 0


def random_palette():
    colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black",
              "blue", "blueviolet", "brown", "chocolate", "coral", "cornflowerblue",
              "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey",
              "darkgreen",
              "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon",
              "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet",
              "deeppink",
              "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia",
              "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew",
              "hotpink",
              "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
              "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightgray", "lightgrey",
              "lightpink",
              "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue",
              "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue",
              "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
              "mediumturquoise",
              "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace",
              "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
              "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple",
              "rebeccapurple",
              "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna",
              "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan",
              "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow",
              "yellowgreen"]

    bw = ["black", "white"]

    palette = [colors, bw]
    return random.choice(palette)


def generate_image(width, height, patch: bool, lines: bool, polygon: bool, eclipse: bool, rectangle: bool):
    image = Image.new(color_scheme, (width, height), random_color())
    draw = ImageDraw.Draw(image)
    if patch is True:
        for i in range(Tech.random_int(min, height)):
            image.paste((random_color()), (
                Tech.random_int(min, width), Tech.random_int(min, height),
                Tech.random_int(min, width),
                Tech.random_int(min, height)))

    for i in range(random.randint(min, 50)):
        if lines is True:
            draw.line(random_parameters(height), fill=ImageColor.getrgb(random_color()))
        else:
            pass
        if polygon is True:
            draw.polygon(random_polygon(width, height), fill=random_color(), outline=random_color())
        else:
            pass

    for j in range(random.randint(min, 5)):
        if eclipse is True:
            draw.ellipse(random_parameters(width), fill=ImageColor.getcolor(random_color(), color_scheme))
        else:
            pass

    for x in range(random.randint(min, 10)):
        if rectangle is True:
            draw.rectangle(random_parameters(width), fill=ImageColor.getcolor(random_color(), color_scheme))
        else:
            pass
    image.save(Tech.create_random_filename())


def random_parameters(upper_range):
    return (random.randint(min, upper_range), random.randint(min, upper_range),
            random.randint(min, upper_range), random.randint(min, upper_range))


def random_polygon(x, y):
    try:
        length = random.randint(2, 500)
        polygon_x = random.sample(range(1, x), length)
        polygon_y = random.sample(range(1, y), length)
        return polygon_x + polygon_y
    except Exception as error:
        print(error)
        pass


def random_color():
    return random.choice(random_palette())
