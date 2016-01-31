#!/usr/bin/env python
# -*- encoding: utf8 -*-
import text_art
import Image

if __name__ == '__main__':
    logos = [
        ['Python', './arts/python.png', './arts/python.md'],
        ['Bugginho Developer', './arts/buginho.png', './arts/buguinho-develop.md'],
        ['Java', './arts/java.jpg', './arts/java.md'],
    ]

    for logo in logos:
        image = Image.open(logo[1])
        with open(logo[2], 'w') as markdown:
            markdown.write('# %s\n\n````\n' % logo[0])
            for line in text_art.image_to_textart(image):
                markdown.write('%s\n' % ''.join(line))
            markdown.write('````')
