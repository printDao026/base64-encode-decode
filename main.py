import base64
#neden utf-8 çünkü utf-8 hem metin hemde sayıları ve sembolleri destekliyor olması ve base64 gibi bir hash türüdür

discord="dao026"#bana burdan ulaşabilirsiniz

while True:
    try:
        banner = """
        ****************    
        *1.base64 decode*
        *2.base64 encode*
        ****************
        """
        print(banner)
        deger = int(input("Arasından birisini seçiniz: "))
        
        if deger == 1:
            base64kod = input("base64 kodunuzu atınız: ")
            decoded_data = base64.b64decode(base64kod)#burda base64kod değişkenini decode ediyoruz
            print("**************************************************************")
            print(decoded_data.decode("utf-8"), "decode edilmiştir eğer base64 ise")
        elif deger == 2:#burda elif yazma sebebimiz yukardaki if cümlesi yanlışsa alttaki elif koşuluna geçmesi siz burda else de diyebilirdiniz
            base64kod1 = input("mesajınızı atınız: ")
            bayt_veri = base64kod1.encode("utf-8")#base64kod1 değerı utf-8 dönüştürüyoruz
            kod = base64.b64encode(bayt_veri)#burda base64 encode ediyoruz yani yazdığım kelimeyi base64 dönüştürüyor
            print("**************************************************************")
            print(kod.decode(), "encode edilmiştir")
    except ValueError:
        print("****************************************************************************")
        print("seçtiğiniz değer base64 yanındaki olmalıdır veya attığınız base64 kod hatalı")


   