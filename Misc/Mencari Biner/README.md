# Mencari Biner

![Chall ss](https://i.postimg.cc/0ydG4w2g/image.png)

## 📂 Resources
Service : `nc 167.71.212.18 64896`

File    : [chall.py](./chall.py)

## ✅ Solutions

Diberikan sebuah network service beserta dengan source code nya.
Hal pertama yang harus dilakukan adalah menganalisa program tersebut dari file yang sudah diberikan, dan ternyata dari program ini kita diminta untuk menebak sebuah angka random, berikut algoritma programnya

1. Melakukan 100 kali perulangan
2. Men-generate random angka antara 1 - 100
3. Disetiap perulangan ada 7 kali kesempatan menebak angka, jika benar nilai poin bertambah 1, dan jika salah program berhenti
4. Jika nilai poin kita 100, maka akan diberikan sebuah flag

Dari schema algoritma diatas kita bisa tahu ada 100 kemungkinan angka dan hanya ada 7 kesempatan untuk menjawab, artinya jika ditebak manual pasti akan sulit sekali, jadi kita bisa melakukan automasi script.

Sesuai dengan nama soal yaitu **Mencari Biner** ini merujuk ke salah satu algoritma pencarian *Binary Search*, artinya kita bisa menyelesaikan soal ini dengan menerapkan algoritma tersebut dan disesuaikan dengan programnya.

Saya sudah membuat script [solver.py](./solver.py) untuk melakukan automasi nya, dan berikut hasilnya:

![Hasil ss solver.py](https://i.ibb.co/S7dtRrQ/image.png)

<div align="center">

## 🏳️ Flag: TCP1P{b1n4ry_s3arch1ng_637266520}

</div>