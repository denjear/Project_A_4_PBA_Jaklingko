# 🧠 Analisis Sentimen Artikel Berita Layanan Transportasi JakLingko

## 📘 Overview  
Jak Lingko merupakan sistem integrasi transportasi publik di Jakarta yang dirancang untuk menyatukan berbagai moda transportasi dalam satu platform, baik dari sisi pembayaran maupun rute perjalanan.  
Meskipun memiliki tujuan untuk mendukung konsep *Mobility as a Service (MaaS)* dan pengembangan *smart city*, aplikasi ini sering menjadi sorotan publik.  

Beberapa media menyoroti kemudahan dan inovasinya, sementara yang lain menyoroti kendala teknis dan layanan.  
Melalui pendekatan **sentiment analysis** terhadap teks berita daring, proyek ini bertujuan untuk memahami persepsi publik terhadap aplikasi Jak Lingko secara objektif dan berbasis data.

---

## 🎯 Problem Statements  
1. Bagaimana persepsi masyarakat terhadap aplikasi Jak Lingko sebagaimana tercermin dalam pemberitaan media online?  
2. Bagaimana distribusi sentimen (positif, negatif, atau netral) pada teks berita yang membahas aplikasi Jak Lingko?  
3. Aspek apa saja dari layanan Jak Lingko yang paling banyak menimbulkan sentimen tertentu (positif atau negatif)?  
4. Bagaimana hasil analisis ini dapat memberikan rekomendasi bagi pengembangan layanan aplikasi Jak Lingko?

---

## 🧠 Objectives  
- Menganalisis persepsi publik terhadap aplikasi Jak Lingko melalui berita daring.  
- Mengklasifikasikan berita menjadi kategori sentimen positif, negatif, dan netral.  
- Mengidentifikasi aspek layanan yang paling sering muncul dalam sentimen publik.  
- Memberikan *insight* dan rekomendasi berdasarkan hasil analisis.  

---

## 🗂️ Dataset  
Dataset dikumpulkan melalui teknik **web scraping** dari portal berita daring seperti **Kompas**, **Tempo**, dan sejenisnya.  

**Struktur dataset final:**

| Kolom | Deskripsi |
|-------|------------|
| `title` | Judul artikel berita |
| `source` | Sumber atau nama media |
| `date` | Tanggal publikasi |
| `url` | Tautan berita asli |
| `article_text` | Isi lengkap berita |
| `label` | Kategori artikel (opinion, news, government) |

---

## ⚙️ Methodology  

1. **Data Collection (Scraping Berita)**  
   Data dikumpulkan melalui proses *web scraping* dari berbagai portal berita daring menggunakan `Selenium` dan `Requests`.  
   Proses ini menghasilkan kumpulan artikel berita yang membahas aplikasi **Jak Lingko** dari berbagai sumber seperti **Kompas**, **Tempo**, dan media nasional lainnya.  

2. **Text Preprocessing**  
   Teks berita dibersihkan dengan menghapus tanda baca, angka, URL, dan duplikasi.  
   Selanjutnya dilakukan *case folding*, *tokenization*, *stopword removal*, serta *stemming* menggunakan library `Sastrawi` untuk menormalkan kata ke bentuk dasar.  

3. **Exploratory Data Analysis (EDA)**  
   Dilakukan analisis eksploratif untuk memahami pola dan karakteristik teks.  
   Tahapan ini mencakup analisis frekuensi kata, visualisasi *word cloud*, serta pengamatan distribusi kata kunci atau topik yang sering muncul.  

4. **Feature Extraction: TF-IDF, POS Tagging, dan NER**  
   - **TF-IDF (Term Frequency–Inverse Document Frequency):** Digunakan untuk mengekstraksi kata penting dari korpus berita.  
   - **POS Tagging (Part-of-Speech):** Mengidentifikasi peran gramatikal kata (kata benda, kerja, sifat, dll) menggunakan model NLP bahasa Indonesia.  
   - **NER (Named Entity Recognition):** Mengenali entitas seperti nama tempat, organisasi, dan tokoh yang sering disebut dalam konteks berita tentang Jak Lingko.  

5. **Insights & Interpretation**  
   Dari hasil analisis teks dan fitur linguistik, diperoleh wawasan mengenai persepsi publik terhadap aplikasi Jak Lingko.  
   Tahap ini menyoroti topik atau isu yang paling banyak dibahas serta sentimen implisit yang muncul dalam pemberitaan media daring.


---

## 🧾 Tools & Libraries  

- **Python 3.x**  
- **Selenium / News** – Web scraping  
- **Sastrawi** – NLP preprocessing  
- **Matplotlib / Seaborn / WordCloud** – Visualization  

---

## 📊 Expected Output  

- Distribusi sentimen publik terhadap aplikasi Jak Lingko.  
- Word cloud dan grafik frekuensi kata dominan.  
- Insight terhadap aspek layanan yang paling banyak dibahas dalam berita.  
- Rekomendasi perbaikan berdasarkan hasil analisis sentimen.  

---

## 🧩 Folder Structure  

```text
📂 (root)
├── datasets/
│
├── notebooks/
|
├── paper/
│   └── ProjectA_Kelompok_4_JakLingko.pdf
│
└── README.md
```
---

## 👩‍💻 Author  

- **Faiz Musyaffa Ramadhan - 5026221153**
- **Muhammad Irsyad Fahmi - 5026221187**
---

Undergraduate Information Systems  
📍 Institut Teknologi Sepuluh Nopember Surabaya, 2025  

---
