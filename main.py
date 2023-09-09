"""
aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""

"""

from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)

kode diatas benar, tapi kurang direkomendasikan, yang lebih direkomendasikan adalah
bila ditulis dengan tulisan dibawah ini
"""



import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)