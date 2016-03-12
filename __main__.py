#!/usr/bin/env python
# -*- encoding: utf8 -*-
import text_art
from PIL import Image

if __name__ == '__main__':
    logos = [
        ['Python', './arts/python.png', './arts/python.md'],
        ['Devry', './arts/devry.jpg', './arts/devry.md'],
        ['Bugginho Developer', './arts/buginho.png', './arts/buguinho-develop.md'],
        ['Java', './arts/java.jpg', './arts/java.md'],
        ['RaulHc', './arts/raulhc.png', './arts/raulhc.md'],
    ]

    for logo in logos:
        image = Image.open(logo[1])
        with open(logo[2], 'w') as markdown:
            markdown.write('# %s\n\n````\n' % logo[0])
            for line in text_art.image_to_textart(image):
                markdown.write('%s\n' % ''.join(line))
            markdown.write('````')
