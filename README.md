# 🍰 Python Malzeme Kontrol Sistemi (Set Kullanımı)

Bu, Python'ın **Set (Küme)** veri yapısının özelliklerini kullanarak iki farklı malzeme listesini karşılaştıran basit bir komut satırı uygulamasıdır. Kullanıcıdan alınan malzemeler ile belirlenen bir tarifin malzemeleri arasındaki eksik ve fazla olanları hızlıca tespit eder.

## ✨ Temel Özellikler

* **Verimli Kıyaslama:** Eksik ve ekstra malzemeleri bulmak için Set farkı alma (`-`) operatörünü kullanır, bu da kodun okunabilirliğini ve hızını artırır.
* **Büyük/Küçük Harf Toleransı:** Kullanıcıdan alınan tüm girdileri otomatik olarak küçük harfe çevirir ve boşlukları temizler, böylece yanlış eşleşmeleri önler.
* **Temiz Çıktı:** Sonuçlar (`missing_ingredients`, `extra_ingredients`) kullanıcıya düzenli, virgülle ayrılmış bir dize olarak sunulur.

## 🚀 Nasıl Çalıştırılır?

### Ön Gereksinimler

Sisteminizde **Python 3.x** kurulu olmalıdır.

### Kurulum ve Çalıştırma

1.  Bu depoyu yerel bilgisayarınıza klonlayın veya indirin.
2.  Uygulama dosyanızı (örneğin `malzeme_kontrol.py`) terminalde çalıştırın:
    ```bash
    python malzeme_kontrol.py
    ```

### Kullanım

Programı çalıştırdıktan sonra, sizden elinizdeki malzemeleri **virgülle ayırarak** girmeniz istenecektir:
Uygulama, bu girdiyi tarife göre analiz edip eksik ve fazla malzemeleri listeleyecektir.

---

## 💻 Proje Detayları

* **Dil:** Python 3.x
* **Temel Yapı:** Setler (Kümeler)
* **Kullanılan Operasyon:** Set Farkı (`-`)

---