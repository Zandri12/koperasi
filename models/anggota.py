from odoo import models, fields

class KoperasiAnggota(models.Model):
    _inherit = 'res.partner'

    is_koperasi_anggota = fields.Boolean(string='Anggota Koperasi', default=False)
    nomor_anggota = fields.Char(string='Nomor Anggota')
    tanggal_gabung = fields.Date(string='Tanggal Gabung')
    # Tambahkan field lain sesuai kebutuhan koperasi 