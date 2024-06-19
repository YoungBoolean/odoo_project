# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookModel(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(required=True)
    description = fields.Text()
    pages = fields.Integer()
    genre_ids = fields.Many2many('library.genre', string="Genres")
    genre_names = fields.Char(compute='_compute_genre_names', store=True, string="Genre Names")
    short_description = fields.Char(string="Short Description", compute='_compute_description')

    @api.depends('description')
    def _compute_description(self):
        for record in self:
            if record.description:
                record.short_description = (record.description[:20] + '...') if len(
                    record.description) > 20 else record.description
            else:
                record.short_description = 'No description'

    @api.depends('genre_ids')
    def _compute_genre_names(self):
        for book in self:
            book.genre_names = ', '.join(book.genre_ids.mapped('name'))


class GenreModel(models.Model):
    _name = 'library.genre'
    _description = 'Genre'

    name = fields.Char(string='Genre', required=True)


class BookIssueModel(models.Model):
    _name = 'library.book.issue'
    _description = 'Book Issue'

    contact_id = fields.Many2one('res.partner', string="Contact", required=True)
    book_ids = fields.Many2many('library.book', string="Books")
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    status = fields.Selection([
        ('reserved', 'Reserved'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='reserved', required=True)
