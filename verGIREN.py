#pip install pyfiglet
import pyfiglet

ascii_banner = pyfiglet.figlet_format("VerGIREN")
print(ascii_banner)


print("Aliexpress'ten Alacaginiz Elektronik Urunler Icin Vergili Hesaplama")
fiyat=float(input("Fiyat Giriniz:\n"))
vergiren=float(fiyat)*0.2
damga_sunum=10.8
toplam=(fiyat)+(vergiren)+(damga_sunum)
print("VerGirenli Toplam:")
print(toplam)
