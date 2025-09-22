import random

# 25 soal tebak negara untuk SMP
questions = [
    {
        "q": "Negara manakah yang dikenal sebagai Negeri Sakura?",
        "choices": ["A. Jepang", "B. Korea Selatan", "C. Cina", "D. Thailand"],
        "answer": "A"
    },
    {
        "q": "Ibu kota dari negara Australia adalah?",
        "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
        "answer": "C"
    },
    {
        "q": "Negara manakah yang benderanya hanya terdiri dari satu warna merah?",
        "choices": ["A. Kanada", "B. Jepang", "C. Cina", "D. Libya (lama)"],
        "answer": "D"
    },
    {
        "q": "Negara terbesar di dunia berdasarkan luas wilayah adalah?",
        "choices": ["A. Amerika Serikat", "B. Kanada", "C. Rusia", "D. Brasil"],
        "answer": "C"
    },
    {
        "q": "Negara manakah yang terkenal dengan piramida?",
        "choices": ["A. Mesir", "B. Yunani", "C. Meksiko", "D. India"],
        "answer": "A"
    },
    {
        "q": "Ibu kota dari negara India adalah?",
        "choices": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "q": "Negara manakah yang menjadi tuan rumah Olimpiade 2016?",
        "choices": ["A. Jepang", "B. Brasil", "C. Inggris", "D. Rusia"],
        "answer": "B"
    },
    {
        "q": "Negara dengan Menara Eiffel berada di?",
        "choices": ["A. Italia", "B. Jerman", "C. Prancis", "D. Spanyol"],
        "answer": "C"
    },
    {
        "q": "Negara tetangga Indonesia yang menggunakan bahasa Melayu adalah?",
        "choices": ["A. Singapura", "B. Malaysia", "C. Brunei Darussalam", "D. Semua benar"],
        "answer": "D"
    },
    {
        "q": "Bendera negara Kanada memiliki gambar?",
        "choices": ["A. Bunga sakura", "B. Daun maple", "C. Pohon kelapa", "D. Bintang"],
        "answer": "B"
    },
    {
        "q": "Negara dengan populasi terbanyak di dunia adalah?",
        "choices": ["A. India", "B. Cina", "C. Amerika Serikat", "D. Indonesia"],
        "answer": "B"
    },
    {
        "q": "Negara manakah yang berbentuk kepulauan dan dijuluki Negeri Kiwi?",
        "choices": ["A. Jepang", "B. Filipina", "C. Selandia Baru", "D. Islandia"],
        "answer": "C"
    },
    {
        "q": "Ibu kota Inggris adalah?",
        "choices": ["A. Liverpool", "B. Manchester", "C. London", "D. Birmingham"],
        "answer": "C"
    },
    {
        "q": "Negara yang dikenal dengan Tembok Besar adalah?",
        "choices": ["A. Jepang", "B. Cina", "C. Korea", "D. Mongolia"],
        "answer": "B"
    },
    {
        "q": "Negara manakah yang memiliki bendera dengan lingkaran merah di tengah putih?",
        "choices": ["A. Jepang", "B. Korea Selatan", "C. Indonesia", "D. Swiss"],
        "answer": "A"
    },
    {
        "q": "Negara yang memiliki gurun Sahara adalah?",
        "choices": ["A. Afrika Selatan", "B. Mesir", "C. Aljazair", "D. Nigeria"],
        "answer": "C"
    },
    {
        "q": "Negara mana yang dikenal dengan sebutan 'Negeri Kincir Angin'?",
        "choices": ["A. Belanda", "B. Swiss", "C. Denmark", "D. Swedia"],
        "answer": "A"
    },
    {
        "q": "Negara tetangga Indonesia yang memiliki kota Dili sebagai ibu kota?",
        "choices": ["A. Papua Nugini", "B. Timor Leste", "C. Malaysia", "D. Brunei"],
        "answer": "B"
    },
    {
        "q": "Negara dengan ibukota Bangkok adalah?",
        "choices": ["A. Vietnam", "B. Thailand", "C. Laos", "D. Kamboja"],
        "answer": "B"
    },
    {
        "q": "Negara manakah yang disebut Negeri Matahari Terbit?",
        "choices": ["A. Cina", "B. Jepang", "C. Korea", "D. Mongolia"],
        "answer": "B"
    },
    {
        "q": "Negara dengan Patung Liberty berada di?",
        "choices": ["A. Kanada", "B. Amerika Serikat", "C. Inggris", "D. Brasil"],
        "answer": "B"
    },
    {
        "q": "Negara yang terkenal dengan keju dan cokelatnya adalah?",
        "choices": ["A. Prancis", "B. Swiss", "C. Belgia", "D. Belanda"],
        "answer": "B"
    },
    {
        "q": "Negara yang terdiri dari ribuan pulau dan terkenal dengan samba?",
        "choices": ["A. Brasil", "B. Indonesia", "C. Filipina", "D. Kuba"],
        "answer": "A"
    },
    {
        "q": "Negara manakah yang memiliki bendera merah putih mirip Indonesia?",
        "choices": ["A. Polandia", "B. Singapura", "C. Monaco", "D. Vietnam"],
        "answer": "C"
    },
    {
        "q": "Negara dengan ibu kota Ankara adalah?",
        "choices": ["A. Mesir", "B. Turki", "C. Yunani", "D. Iran"],
        "answer": "B"
    }
]

def main():
    print("=== KUIS TEBAK NEGARA (25 Soal SMP) ===\n")
    random.shuffle(questions)
    score = 0
    
    for i, q in enumerate(questions, start=1):
        print(f"Soal {i}: {q['q']}")
        for c in q["choices"]:
            print("  ", c)
        jawab = input("Jawaban (A/B/C/D): ").strip().upper()
        if jawab == q["answer"]:
            print("✔ Benar! +4 poin\n")
            score += 4
        else:
            print(f"✘ Salah! Jawaban benar: {q['answer']}\n")
    
    print("=== HASIL AKHIR ===")
    print(f"Skor kamu: {score} dari 100")
    if score >= 80:
        print("Luar biasa! Pengetahuan geografi kamu sangat bagus 🌍")
    elif score >= 60:
        print("Bagus, kamu cukup mengenal dunia 💪")
    else:
        print("Terus belajar mengenal negara-negara di dunia 😉")

if __name__ == "__main__":
    main()