# Insecure

![Chall ss](https://i.ibb.co/WH0qTkt/image.png)

## 📂 Resource

Website: http://ctf.tcp1p.com:16544/

## ✅ Solutions

Diberikan sebuah website, ketika web tersebut pertama kali menampilkan sebuah text *"You are not an admin..."*, dari sini kita bisa tahu berasumsi bahwa untuk mendapatkan flag kita harus mengakses web tersebut sebagai admin.

Sesuai juga dengan deskripsi soal terdapat sebuah kata kunci *cookie* dimana ini menjadi bahwa kita perlu mengganti value *cookie* nya. Kita akan mengecek terlebih dahulu nilai dari *cookie* yang ada.

![default cookie](https://i.ibb.co/44xtCnm/image.png)

ternyata didalamnya ada cookie dengan nama *admin* dan nilainya adalah *0*, dan sepertinya ini bisa dimanipulasi dengan mengubah nilai nya menjadi *1*.

![manipulasi cookie](https://i.ibb.co/vdbZpKv/image.png)

setelah kita mengubah nilai *admin* menjadi *1* dan merefresh halaman web nya kita mendapatkan respon baru dengan tulisan *"Hi admin!"*, tapi tetap tidak ada flag.

Coba cek source dari web nya, dengan cara **ctrl + u**

![view source](https://i.ibb.co/NKFN0Wr/image.png)

dan benar sekali flag nya disembunyikan dan kita bisa melihatnya di view source.

<div align="center">

## 🏳️ Flag: TCP1P{1ns3cUr3_C00k1Es}

</div>