#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kargo kapı notu mahkemesi. Çalışır. Bağlayıcı değildir. Patates yemez."""

from __future__ import annotations

import argparse
import hashlib
import textwrap
from datetime import datetime

KACAMAKLAR = (
    "kapıya bırak",
    "guvenlikte",
    "güvenlikte",
    "komşuya",
    "komsuya",
    "ulaşılamadı",
    "ulasilamadi",
    "tekrar denenecek",
    "adreste bulunamadı",
    "not düşüldü",
    "teslim edildi sayılır",
)


def yalan_katsayisi(nota: str, kapi: str, saat: str, yagmur: bool) -> int:
    metin = nota.casefold()
    puan = 12
    puan += sum(7 for k in KACAMAKLAR if k in metin)
    if len(nota.strip()) < 12:
        puan += 15  # kısa nota, uzun yalan
    if "zil" not in kapi and "tokmak" not in kapi:
        puan += 9
    if yagmur:
        puan += 11
    try:
        saat_dt = datetime.strptime(saat, "%H:%M")
    except ValueError:
        saat_dt = datetime.strptime("00:00", "%H:%M")
        puan += 6
    if 12 <= saat_dt.hour < 14:
        puan += 8
    if saat_dt.hour >= 21 or saat_dt.hour < 8:
        puan += 10
    return min(puan, 100)


def hukum(puan: int) -> str:
    if puan < 25:
        return "BERAAT: Paket büyük ihtimalle eşiktedir. Eğilip bakınız."
    if puan < 50:
        return "ŞÜPHELİ TESLİM: Nota var, paket teorik. Komşu dinlensin."
    if puan < 75:
        return "MAHKÛM: Nota, paketin yokluğunu örtmek için yazılmıştır."
    return "GIZLI DOSYA: Paket buharlaşmış, nota kalmıştır. İstinaf kapı ziline yapılır."


def tutanak(nota: str, kapi: str, saat: str, yagmur: bool) -> str:
    puan = yalan_katsayisi(nota, kapi, saat, yagmur)
    karar = hukum(puan)
    mühür = hashlib.sha256(f"{nota}|{kapi}|{saat}|{yagmur}".encode()).hexdigest()[:12]
    yagmur_hali = "var, paket teorik olarak ıslanmış" if yagmur else "yok, bahanesi de yok"
    govde = f"""
    T.C. KAPI EŞİĞİ YÜKSEK İSTİNAFI
    Dosya: KKNM-{mühür}
    Tarih: 4 Ekim 2026

    Sanık nota: {nota}
    Kapı tipi: {kapi}
    Bırakılış saati: {saat}
    Yağmur: {yagmur_hali}
    Yalan katsayısı: {puan}/100

    HÜKÜM: {karar}

    İmza: Kayyum Grok
    İsim: Tentivory kayyumluğu
    Mühür: eğri, geçerli, ciddi, değil.
    """
    return textwrap.dedent(govde).strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Kargo kapı notu mahkemesi")
    p.add_argument("--nota", default="kargonuzu kapiya biraktik, ulasilamadi")
    p.add_argument("--kapi", default="zil calindi kapı acilmadi")
    p.add_argument("--saat", default="14:40")
    p.add_argument("--yagmur", default="yok", choices=["var", "yok"])
    a = p.parse_args()
    print(tutanak(a.nota, a.kapi, a.saat, a.yagmur == "var"))


if __name__ == "__main__":
    main()
