{
    'name': 'Koperasi Simpan Pinjam',
    'version': '16.0.1.0.0',
    'summary': 'Modul koperasi simpan pinjam terintegrasi dengan kontak',
    'category': 'Custom',
    'author': 'Pengguna',
    'depends': ['base', 'contacts'],
    'data': [
        'views/anggota_views.xml',
        'views/simpanan_views.xml',
        'views/pinjaman_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
} 