# Magic

![Chall ss](https://i.ibb.co/XyqTtCW/image.png)

## 📂 Resources

Website: http://ctf.tcp1p.com:45659/

File: [chall.php](./chall.php)

## ✅ Solutions

Diberikan sebuah website beserta dengan source code nya, ketika website tersebut pertama kali diakses terdapat teks *"Please specify secret in the GET parameter!"*, setelah itu saya menambahkan parameter *secret* di url dengan random dan muncul teks *"Invalid secret!"*. Okee kita perlu membaca source code untuk mengetahui nilai *secret* yang benar.

![true secret](https://i.ibb.co/JjKxWdt/image.png)

kode diatas adalah penentu agar kita bisa mendapatkan flag nya, jika dilihat kita bisa melakukan **Type Jugling** untuk membuat statementnya menjadi **true**.

setelah mencari **Type Jugling** yang pas saya menemukan bahwa value **QNKCDZO** yang diconvert ke *md5* dapat membuat statement diatas menjadi **true**.

> Sumber: https://stackoverflow.com/questions/22140204/why-md5240610708-is-equal-to-md5qnkcdzo

Berarti kita bisa langsung menginputkan value tersebut ke parameter secret nya.

![hasil akhir](https://i.ibb.co/SJQmVLY/image.png)

dan kita berhasil mendapatkan flag nya, dengan vuln **Type Jugling** dari PHP.

<div align="center">

## 🏳️ Flag: TCP1P{W31rD_PHP_B3h4v10rS}

</div>