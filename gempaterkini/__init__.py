import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    Tanggal: 09 September 2023, 12:02:51 WIB
    Magnitudo: 5.0
    Kedalaman: 210 km
    Lokasi: 7.62 LS - 128.54 BT
    Pusat Gempa: 101 km TimurLaut MALUKUBRTDAYA
    Dirasakan: tidak berpotensi TSUNAMI
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        # kode dibawah ini untuk mencari title dengan menggunakan beautifulsoup
        # title = soup.find('title')
        # dibawah ini adalah cara mencari tanggal dari bmkg dengan kata kunci css inspect element
        result = soup.find('span', {'class': 'waktu'})
        # split digunakan untuk memecah 2 data
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi {result['lokasi']}")
    print(f"koordinat LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('ini adalah gempa terkini')
    print('hai')

