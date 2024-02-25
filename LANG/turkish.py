from colorama import Fore, Style

from projekt import general


langpac_revision = "1"


ascii_title = """
 OBERWISSENFUHRER YAKUP ASLANTAS TARAFINDAN KODLANDI
██████╗  ██████╗ ██████╗ ███████╗███████╗██╗███╗   ██╗
██╔══██╗██╔════╝██╔═══██╗██╔════╝██╔════╝██║████╗  ██║
██║  ██║██║     ██║   ██║█████╗  █████╗  ██║██╔██╗ ██║
██║  ██║██║     ██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║
██████╔╝╚██████╗╚██████╔╝██║     ██║     ██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝
                     OBERWISSEN
                   t.me/oberwissen
"""

cmd_title = f"dcoffin {general.version} - TR {langpac_revision} - t.me/oberwissen"

start_menu = f"""
BİR SEÇENEK SEÇİN

    --------------- DCOFFIN
    {Fore.CYAN}0{Fore.RESET}|  ÇIKIŞ
    {Fore.CYAN}1{Fore.RESET}|  Güncellemeleri Denetle
    
    --------------- DISCORD
    {Fore.CYAN}2{Fore.RESET}|  Normal Spam
    {Fore.CYAN}3{Fore.RESET}|  Değişiklik Günlüğü
"""


not_a_option = f"{Fore.RED}{Style.BRIGHT} [ ! ] {Style.RESET_ALL} Öyle bir seçenek yok."
thanks_and_bye = "Ürünümüzü kullandığınız için teşekkür ederiz! - t.me/oberwissen"
update_available = "yeni bir güncelleme mevcut, yüklemek istiyor musunuz? ( y = evet / n = hayır )"
restart_text = "Yeniden başlatılıyor..."
spam_tutorial = """
1. Tokeninizi alıp discord/tokens.txt ye yapıştırın ( 1den fazla token kullanmak için yeni satıra geçin )
2. Spam atmak istediğiniz discord kanalının ID sini discord/channel_ids.txt ye yapıştırın ( 1den fazla kanal id kullanmak istiyorsanız yeni satıra geçin )

Bu adımları tamamladıktan sonra [ ENTER ] tuşuna tıklayıp devam edebilirsiniz.
"""
message = "Mesaj : "
delay = "Bekleme süresi : "
spam_started = "Spam işlemi başladı, eğer ters giden bir durum olursa bilgilendirileceksiniz."
cant_import_module = "Bu uygulama bir modül olarak kullanılmak üzere tasarlanmamıştır."
empty_message_error = "Lütfen bir mesaj girin."
please_enter_valid_num = "Lütfen geçerli bir sayı girin"
invalid_token = "Geçersiz token"
access_denied = "Erişim reddedildi"
checking_updates = "Güncellemeler denetleniyor..."
updating = "Güncelleniyor... Lütfen bekleyin"
update_success = "Güncelleme başarılı, etkili olması için yeniden başlatın."
enter_to_return = "Geri dönmek için [ ENTER ] tuşuna basın"


whats_new = """
dcoffin versiyon 0.0.1 ---------

 - İlk sürüm
"""


if __name__ == "__main__":
    print(ascii_title)
    print(cmd_title)
    print(start_menu)