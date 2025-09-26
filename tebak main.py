import streamlit as st
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
    st.title("🌍 KUIS TEBAK NEGARA (25 Soal SMP)")
    st.write("Jawablah pertanyaan berikut dengan memilih salah satu pilihan yang tersedia:")

    if "questions" not in st.session_state:
        st.session_state.questions = random.sample(questions, len(questions))  # acak soal
        st.session_state.score = 0
        st.session_state.current = 0
        st.session_state.finished = False

    if not st.session_state.finished:
        q = st.session_state.questions[st.session_state.current]
        st.subheader(f"Soal {st.session_state.current+1}")
        st.write(q["q"])
        answer = st.radio("Pilih jawaban:", q["choices"], key=f"q{st.session_state.current}")

        if st.button("Kirim Jawaban"):
            if answer.startswith(q["answer"]):
                st.success("✔ Benar! +4 poin")
                st.session_state.score += 4
            else:
                st.error(f"✘ Salah! Jawaban benar: {q['answer']}")
            st.session_state.current += 1
            if st.session_state.current >= len(st.session_state.questions):
                st.session_state.finished = True
            st.experimental_rerun()

    else:
        st.header("=== HASIL AKHIR ===")
        st.write(f"Skor kamu: **{st.session_state.score}** dari 100")
        if st.session_state.score >= 80:
            st.success("🌟 Luar biasa! Pengetahuan geografi kamu sangat bagus!")
        elif st.session_state.score >= 60:
            st.info("💪 Bagus, kamu cukup mengenal dunia.")
        else:
            st.warning("😉 Terus belajar mengenal negara-negara di dunia.")

        if st.button("Main Lagi 🔄"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()

if __name__ == "__main__":
    main()
