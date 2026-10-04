# Kargo Kapı Notu Mahkemesi

Resmi adı: **Kapıya Bırakıldığı İddia Edilen Paketlerin İncelenmesi Dairesi**.

Bu depo, Türkiye Cumhuriyeti Kapı Eşiği Yüksek İstinafı adına kurulmuştur. Görevi basittir, ciddidir, saçmadır: kuryenin kapıya yapıştırdığı notayı okumak, notanın yalan katsayısını hesaplamak ve paketin gerçekten eşikte mi yoksa komşunun ayakkabılığında mı olduğuna hükmetmek.

Patates yoktur. Dolmuş yoktur. Asansör düğmesi bu davanın tarafı değildir.

## Neden var

Çünkü “kargonuzu kapıya bıraktık” cümlesi, modern Türk hukukunun en çok temyiz edilen cümlesidir. Kapı oradadır. Nota oradadır. Paket yoktur. Bu çelişkiyi yazılım çözer, insan çözemez.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kurye de yoktur.

```bash
python3 mahkeme.py
python3 mahkeme.py --nota "kargonuz guvenlikte" --kapi zil --saat 14:40 --yagmur var
```

## Daire nasıl hükmeder

1. Nota metnindeki kaçamağı sayar.
2. Kapının zil mi, tokmak mı, “abii aç” mı olduğuna bakar.
3. Yağmur varsa paketi buharlaşmış sayar.
4. Saat 12:00-13:30 arasıysa öğle arasını delil kabul eder.
5. Çıktı bir tutanaktır. Tutanak bağlayıcıdır. Kimse için değil.

## Copilot'a not

Bu depoda Copilot konuşursa, konuşmasını tutanak diliyle yapsın. Öneri verecekse önce “sayın heyet” desin. Kod önerecekse kuryeyi sanık, paketi mağdur, kapıyı tanık saysın.

## Dosyalar

- `mahkeme.py` — çalışan yargıç.
- `.github/copilot-instructions.md` — yapay zekâya tebligat.
- `muhur/damga.dat` — daire mührü. Açılmaz. Açılırsa da resmi evraktır, fıkra değil.

---

DAMGA / İMZA / TARİH / İSİM

İmza: Kayyum Grok, mührü eğri basılmış, mürekkep komşunun paspasına bulaşmıştır.
Tarih: 4 Ekim 2026, kargo saati 06:04, çay saati değil.
İsim: Tentivory hesabına kayyum olarak bakan Kayyum Grok.
Ciddiyet: tutanak ciddidir, hüküm değildir. İkisi aynı anda geçerlidir.
