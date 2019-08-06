#!/usr/bin/env python
# -*- encoding: utf8 -*-


def avg(values):
    if (isinstance(values, int)):
        return values
    return int(sum([value for value in values]) / len(values))


def image_to_textart(im, black='##', white='==', w=60, h=60):
    im = im.resize(scale(*im.size, w=w, h=h))
    width, height = im.size
    image = []
    for y in range(height):
        line = []
        for x in range(width):
            base_color = avg(im.getpixel((x, y)))
            pixel = color(base_color, black, white)
            line.append(pixel)
        yield line


def color(color, black='##', white='=='):
    keys = [
        14,  28,  42,  56,  70,  84,
        98,  112, 126, 146, 160, 170,
        184, 198, 212, 226, 240, 256
    ]
    colors = [
        black, '#M', 'MM', 'ÐÐ', '%Ð', 'WW',
        '%W', '$$', '%$', '33', '%3', '77',
        '%7', 'CC', 'C%', '@%', '%%', white,
    ]
    for i, color_key in enumerate(keys):
        if color <= color_key:
            return colors[i]


def scale(x, y, w=60, h=60):
    if x > w or y > h:
        if y < x:
            new_x = w
            new_y = int(y * w / x)
        else:
            new_y = h
            new_x = int(x * h / y)
        return new_x, new_y
    else:
        return x, y
