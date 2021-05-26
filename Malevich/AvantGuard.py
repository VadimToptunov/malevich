from PIL import Image, ImageColor, ImageDraw
import random
import MulticolorPatch

color_scheme = "RGB"


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


def generate_with_lines(image_num, width, height):
    for num in range(image_num):
        image = Image.new(color_scheme, (width, height), random_color())
        draw = ImageDraw.Draw(image)
        for i in range(random.randint(0, 50)):
            draw.line(random_parameters(height), fill=ImageColor.getrgb(random_color()))
            draw.polygon(random_polygon(width, height), fill=random_color(), outline=random_color())
        draw_without_lines(draw, width)
        image.save(MulticolorPatch.create_random_filename())


def generate_without_lines(image_num, width, height):
    for num in range(image_num):
        image = Image.new(color_scheme, (width, height), random_color())
        draw = ImageDraw.Draw(image)
        draw_without_lines(draw, width)
        image.save(MulticolorPatch.create_random_filename())


def draw_without_lines(draw, width):
    for j in range(random.randint(0, 5)):
        draw.ellipse(random_parameters(width), fill=ImageColor.getcolor(random_color(), color_scheme))

    for x in range(random.randint(0, 10)):
        draw.rectangle(random_parameters(width), fill=ImageColor.getcolor(random_color(), color_scheme))


def random_parameters(upper_range):
    return (random.randint(0, upper_range), random.randint(0, upper_range),
            random.randint(0, upper_range), random.randint(0, upper_range))


def random_polygon(x, y):
    length = random.randint(1, 500)
    polygon_x = random.sample(range(1, x), length)
    polygon_y = random.sample(range(1, y), length)
    return polygon_x + polygon_y


def random_color():
    return random.choice(random_palette())
