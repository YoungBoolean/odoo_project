# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookModel(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    pages = fields.Integer(string='Number of Pages')
    genre_ids = fields.Many2many('library.genre', string='Genres')


class GenreModel(models.Model):
    _name = 'library.genre'
    _description = 'Genre'

    name = fields.Char(string='Genre', required=True)
