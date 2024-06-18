# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookModel(models.Model):
    _name = 'library.book'
    _description = 'Book Model'

    name = fields.Char(required=True)
    description = fields.Text()
    pages = fields.Integer()
    genre_ids = fields.Many2many('library.genre', string="Genres")
    genre_names = fields.Char(compute='_compute_genre_names', store=True, string="Genre Names")

    @api.depends('genre_ids')
    def _compute_genre_names(self):
        for book in self:
            book.genre_names = ', '.join(book.genre_ids.mapped('name'))


class GenreModel(models.Model):
    _name = 'library.genre'
    _description = 'Genre'

    name = fields.Char(string='Genre', required=True)
