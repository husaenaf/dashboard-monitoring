"""
aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():

    """

    Tanggal: 09 September 2023, 12:02:51 WIB
    Magnitudo: 5.0
    Kedalaman: 210 km
    Lokasi: 7.62 LS - 128.54 BT
    Pusat Gempa: 101 km TimurLaut MALUKUBRTDAYA
    Keterangan: tidak berpotensi TSUNAMI
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '9 S eptember 2023'
    hasil['waktu'] = '12:02:51 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls': 7.62, 'bt': 128.54}
    hasil['pusat'] = '101 km TimurLaut MALUKUBRTDAYA'
    hasil['keterangan'] = 'tidakk berpotensi TSUNAMI'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"lokasi LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat {result['pusat']}")
    print(f"keterangan {result['keterangan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
