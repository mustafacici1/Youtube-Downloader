import yt_dlp

def download_video(url):
    # Video indirme için ayarlar
    ydl_opts = {
        'format': 'best',  # En iyi kaliteyi seçer
        'outtmpl': '%(title)s.%(ext)s',  # Videoyu mevcut dizine indirir ve video başlığını kullanarak kaydeder
        'quiet': False  # Konsolda indirme süreci hakkında bilgi verir
    }

    # Video indirme işlemi
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Örnek kullanım:
video_url = input("url giriniz:")  # Buraya indirmek istediğiniz YouTube video linkini koyun
download_video(video_url)
import yt_dlp

def download_video(url):
    # Video indirme için ayarlar
    ydl_opts = {
        'format': 'best',  # En iyi kaliteyi seçer
        'outtmpl': '%(title)s.%(ext)s',  # Videoyu mevcut dizine indirir ve video başlığını kullanarak kaydeder
        'quiet': False  # Konsolda indirme süreci hakkında bilgi verir
    }

    # Video indirme işlemi
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Örnek kullanım:
video_url = input("url giriniz:")  # Buraya indirmek istediğiniz YouTube video linkini koyun
download_video(video_url)
