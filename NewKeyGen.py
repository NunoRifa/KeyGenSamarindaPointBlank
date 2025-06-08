import requests
import re
import urllib3
import pyperclip
import msvcrt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate_token(hwid):
    session = requests.Session()
    
    headers_browser = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://generatetoken.my.id',
    'Referer': 'https://generatetoken.my.id/samarinda/',
    'Sec-CH-UA': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    # 'Content-Length': '53',  # Tidak perlu ditentukan secara manual, akan dihitung otomatis
    # 'Priority': 'u=0, i',    # Tidak wajib, dan jarang digunakan
    }


    data = {
        'hwid': hwid,
        'generate_token': ''
    }

    try:
        response = session.post(
            'https://generatetoken.my.id/samarinda/',
            data=data,
            headers=headers_browser,
            verify=False
        )
    except requests.exceptions.RequestException as e:
        print("Gagal submit Licensed Key:", e)
        return None

    print("==== Mencari token ====")

    match = re.search(r"html:\s*\"<p id='generated-token'>(.*?)</p>\"", response.text)

    if match:
        token = match.group(1)
        print("Token ditemukan:", token)
        return token
    else:
        print("Token tidak ditemukan.")
        return None

if __name__ == "__main__":
    hwid = input("Masukkan Licensed Key (hex 32 karakter): ").strip()
    token = generate_token(hwid)
    
    if token:
        pyperclip.copy(token)
        print("Token telah disalin ke clipboard.")
    else:
        print("Token gagal didapatkan.")
    
    print("Tekan sembarang tombol untuk keluar...")
    msvcrt.getch()