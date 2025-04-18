import requests
import re
import urllib3
import time
import pyperclip
import msvcrt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate_token(hwid):
    session = requests.Session()

    headers_browser = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://generatetoken.my.id',
        'Referer': 'https://generatetoken.my.id/samarinda/TokenBelut.php',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        session.get('https://62.146.236.10/', headers=headers_browser, verify=False)
        print("1. Akses halaman awal berhasil.")
    except requests.exceptions.RequestException as e:
        print("Gagal akses halaman awal:", e)
        return None

    time.sleep(1)

    try:
        session.get('https://generatetoken.my.id/samarinda/TokenBelut.php', headers=headers_browser, verify=False)
        print("2. Akses halaman form berhasil.")
    except requests.exceptions.RequestException as e:
        print("Gagal akses TokenBelut.php:", e)
        return None

    time.sleep(1)

    data = {
        'hwid': hwid,
        'generate_token': ''
    }

    try:
        response = session.post(
            'https://generatetoken.my.id/samarinda/TokenBelut.php',
            data=data,
            headers=headers_browser,
            verify=False
        )
        print("3. Simulasi submit HWID sukses. Response Status:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Gagal submit HWID:", e)
        return None

    print("4. ==== Mencari token ====")

    time.sleep(3)

    match = re.search(r"html:\s*\"<p id='generated-token'>(.*?)</p>\"", response.text)

    if match:
        token = match.group(1)
        print("5. Token ditemukan:", token)
        return token
    else:
        print("5. Token tidak ditemukan dalam script JavaScript.")
        return None

if __name__ == "__main__":
    hwid = input("Masukkan HWID (hex 32 karakter): ").strip()
    token = generate_token(hwid)
    
    if token:
        print("6. Token:", token)
        pyperclip.copy(token)
        print("7. Token telah disalin ke clipboard.")
    else:
        print("6. Token gagal didapatkan.")
    
    print("Tekan sembarang tombol untuk keluar...")
    msvcrt.getch()