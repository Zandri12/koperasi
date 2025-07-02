from odoo import models, fields

class KoperasiPinjaman(models.Model):
    _name = 'koperasi.pinjaman'
    _description = 'Pinjaman Koperasi'

    name = fields.Char(string='No. Pinjaman', required=True)
    anggota_id = fields.Many2one('res.partner', string='Anggota', domain=[('is_koperasi_anggota', '=', True)], required=True)
    tanggal = fields.Date(string='Tanggal', required=True)
    jumlah = fields.Float(string='Jumlah', required=True)
    bunga = fields.Float(string='Bunga (%)')
    tenor = fields.Integer(string='Tenor (bulan)')
    keterangan = fields.Text(string='Keterangan') 