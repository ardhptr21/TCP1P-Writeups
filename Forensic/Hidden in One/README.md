# Hidden in One

![Chall ss](https://i.ibb.co/zsNy8GN/image.png)

# 📂 Resource

File: [chall.zip](./chall.zip)

# ✅ Solutions

Diberikan sebuah file *.zip*, ketika file tersebut diekstrak secara normal keluar sebuah file *flag.txt* namun setelah dibuka ternyata itu adalah fake flag.

Karena hal tersebut saya kemudian menggunakan tools **binwalk** untuk mencari tahu apakah ada file lain didalamnya.

> command: binwalk chall.zip

![hasil binwalk](https://i.ibb.co/Fm9wvxv/image.png)

dan ternyata benar, jika dilihat dari hasil **binwalk** ternyata ada file *PNG* didalamnya, kemudian saya mencoba untuk mengekstrak kembali menggunakan **binwalk**.

> command: binwalk -e chall.zip

![hasil ekstrak binwalk](https://i.ibb.co/1MSkpD9/image.png)

setelah dilakukan ekstrak dan melihat folder hasil ekstrak tersebut, ternyata tidak ada file gambar seperti yang kita harapkan.

Karena hal tersebut saya kemudian menggunakan cara lain yaitu menggunakan **foremost** untuk mengekstraknya.

> command: foremost chall.zip

![hasil foremost](https://i.ibb.co/Pzq54bx/image.png)

dan bisa dilihat setelah melakukan ekstrak menggunakan foremost dan melihat folder output nya ada directory *png* dan jika dilihat isinya ada file *00000000.png*, dan ketika file tersebut dibuka keluar sebuah gambar flag.

![hasil gambar](https://i.ibb.co/nD1DKtP/image.png)

<div align="center">
  
  ## 🏳️ Flag: TCP1P{H1dd3N_1n_Pl41n_S1gHt}

</div>