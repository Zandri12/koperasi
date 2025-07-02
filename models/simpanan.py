from odoo import models, fields

class KoperasiSimpanan(models.Model):
    _name = 'koperasi.simpanan'
    _description = 'Simpanan Koperasi'

    name = fields.Char(string='No. Simpanan', required=True)
    anggota_id = fields.Many2one('res.partner', string='Anggota', domain=[('is_koperasi_anggota', '=', True)], required=True)
    tanggal = fields.Date(string='Tanggal', required=True)
    jumlah = fields.Float(string='Jumlah', required=True)
    keterangan = fields.Text(string='Keterangan') 