import streamlit as st
from pathlib import Path

st.set_page_config(page_title="💕 Двор Екатерины II", page_icon="👑", layout="wide")

# Пути к файлам
ASSETS_DIR = Path("assets")
CATHERINE_IMG = ASSETS_DIR / "catherine.jpg"
ORLOV_IMG = ASSETS_DIR / "orlov.jpg"
POTEMKIN_IMG = ASSETS_DIR / "potemkin.jpg"
ZUBOV_IMG = ASSETS_DIR / "zubov.jpg"
PALACE_IMG = ASSETS_DIR / "palace.jpg"
MUSIC_FILE = ASSETS_DIR / "music.mp3"

# Инициализация
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'
    st.session_state.stats = {'orlov': 0, 'potemkin': 0, 'zubov': 0, 'influence': 10}


def reset():
    st.session_state.game_state = 'start'
    st.session_state.stats = {'orlov': 0, 'potemkin': 0, 'zubov': 0, 'influence': 10}


# Стили
st.markdown("""
<style>
    .main { 
        background: linear-gradient(135deg, #1a1a2e, #16213e); 
        color: #e8dfd0; 
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 { color: #ffd700; text-align: center; }
    .stButton>button { 
        background: linear-gradient(135deg, #8B4513, #CD853F); 
        color: white; border: 2px solid #ffd700; 
        border-radius: 15px; width: 100%; margin: 5px 0;
        font-size: 16px;
    }
    .dialogue { 
        background: rgba(26,26,46,0.9); border: 2px solid #8B4513; 
        border-radius: 15px; padding: 20px; margin: 20px 0;
    }
    .stats { background: rgba(139,69,19,0.3); padding: 10px; border-radius: 10px; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)


# Функция для отображения изображения
def show_image(img_path, caption=None):
    if img_path.exists():
        st.image(str(img_path), caption=caption, use_container_width=True)
    else:
        st.warning(f" Файл {img_path.name} не найден!")


# Боковая панель (только статы)
with st.sidebar:
    st.title("📊 Статы")
    s = st.session_state.stats
    st.markdown(f"""
    <div class='stats'>💖 Орлов: {'❤️' * s['orlov']}{'🤍' * (3 - s['orlov'])}</div>
    <div class='stats'>💖 Потёмкин: {'❤️' * s['potemkin']}{'' * (3 - s['potemkin'])}</div>
    <div class='stats'>💖 Зубов: {'❤️' * s['zubov']}{'🤍' * (3 - s['zubov'])}</div>
    <div class='stats'>⚡ Влияние: {s['influence']}</div>
    """, unsafe_allow_html=True)

# === СЦЕНАРИЙ ===

# Экран 1: Старт
if st.session_state.game_state == 'start':
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        show_image(CATHERINE_IMG, "Екатерина II Великая")
        st.title("👑 ДВОР ЕКАТЕРИНЫ II")
        st.subheader("💕 Романтическая историческая новелла")

        # === ПЛЕЕР С МУЗЫКОЙ ===
        if MUSIC_FILE.exists():
            st.audio(str(MUSIC_FILE), format="audio/mp3", loop=True)
            st.caption("🔊 **Важно:** Нажми Play. Музыка будет играть бесконечно (Loop)!")
        else:
            st.error("❌ Файл music.mp3 не найден в папке assets/")
        # ========================

    st.markdown("---")

    if PALACE_IMG.exists():
        st.image(str(PALACE_IMG), caption="Зимний дворец, 1762 год", use_container_width=True)

    st.markdown("""
    ### 📖 Твоя история:

    Ты — молодой дворянин при дворе Екатерины Великой.

    **Твоя цель:**
    - 💕 Завоевать сердце одного из фаворитов
    - 👑 Построить карьеру при дворе
    - 📜 Влиять на историю России

    **Выбирай мудро:** каждый выбор меняет отношения!
    """)

    if st.button("🎮 НАЧАТЬ ИГРУ", type="primary"):
        st.session_state.game_state = 'scene1'
        st.rerun()

# Экран 2: Выбор героя
elif st.session_state.game_state == 'scene1':
    st.title("📅 1762 год — Прибытие ко двору")

    if PALACE_IMG.exists():
        st.image(str(PALACE_IMG), use_container_width=True)

    st.markdown("""
    Ты только что прибыл в Петербург. 
    В воздухе витает напряжение: Пётр III непопулярен,
    гвардия недовольна, а Екатерина готовится к действию...

    **К кому ты обратишься первым?**
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        show_image(ORLOV_IMG, "Григорий Орлов")
        if st.button("🎖️ Григорий Орлов\n(Герой, гвардеец)"):
            st.session_state.stats['orlov'] += 1
            st.session_state.stats['influence'] += 1
            st.session_state.game_state = 'orlov_path'
            st.rerun()

    with col2:
        show_image(POTEMKIN_IMG, "Григорий Потёмкин")
        if st.button("🏛️ Григорий Потёмкин\n(Стратег, умница)"):
            st.session_state.stats['potemkin'] += 1
            st.session_state.stats['influence'] += 1
            st.session_state.game_state = 'potemkin_path'
            st.rerun()

    with col3:
        show_image(ZUBOV_IMG, "Платон Зубов")
        if st.button("💎 Платон Зубов\n(Красавчик, фаворит)"):
            st.session_state.stats['zubov'] += 1
            st.session_state.game_state = 'zubov_path'
            st.rerun()

# Экран 3: Путь Орлова
elif st.session_state.game_state == 'orlov_path':
    st.title("⚔️ Путь с Орловым")

    col1, col2 = st.columns([1, 2])
    with col1:
        show_image(ORLOV_IMG, "Григорий Орлов")

    with col2:
        st.markdown("""
        **Григорий Орлов** встречает тебя в казармах:

        > *«Новое лицо? У тебя решительный взгляд. 
        > Мне нужны люди, на которых можно положиться. 
        > Готов служить России... и мне?»*
        """)

    choice = st.radio("Твой ответ:", [
        "«Клянусь, моя шпага — в твоих руках!»",
        "«Я служу Императрице, а не людям»",
        "«Расскажите, что от меня требуется»"
    ])

    if st.button("➡️ Продолжить"):
        if "шпага" in choice:
            st.session_state.stats['orlov'] += 2
            st.session_state.game_state = 'orlov_romance'
        elif "Императрице" in choice:
            st.session_state.stats['influence'] += 1
            st.session_state.game_state = 'orlov_political'
        else:
            st.session_state.stats['orlov'] += 1
            st.session_state.game_state = 'orlov_smart'
        st.rerun()

# Экран 4: Романтика Орлова
elif st.session_state.game_state == 'orlov_romance':
    st.title("💕 Роман с Орловым")

    col1, col2 = st.columns([1, 2])
    with col1:
        show_image(ORLOV_IMG, "Григорий Орлов")

    with col2:
        st.markdown("""
        Орлов улыбается и приглашает тебя на ночную прогулку:

        > *«Знаешь, мало кто видит Петербург таким... тихим. 
        > Только луна, Нева и мы. Ты не боишься быть со мной?»*

        **Твоё сердце бьётся чаще...**
        """)

    if st.button(" «С вами — никогда не боюсь»"):
        st.session_state.stats['orlov'] += 3
        st.session_state.game_state = 'ending_orlov'
        st.rerun()

    if st.button("🤝 «Я здесь ради дела»"):
        st.session_state.stats['influence'] += 2
        st.session_state.game_state = 'ending_political'
        st.rerun()

# Экран 5: Политика Орлова
elif st.session_state.game_state == 'orlov_political':
    st.title("🏛️ Политический путь")
    show_image(ORLOV_IMG, "Григорий Орлов")
    st.markdown("Орлов уважает твою независимость. Ты становишься влиятельным придворным.")
    if st.button("Завершить"):
        st.session_state.game_state = 'ending_political'
        st.rerun()

# Экран 6: Умный выбор Орлова
elif st.session_state.game_state == 'orlov_smart':
    st.title(" Мудрый выбор")
    show_image(ORLOV_IMG, "Григорий Орлов")
    st.markdown("Ты проявляешь осторожность. Орлов ценит твой ум.")
    if st.button("Завершить"):
        st.session_state.game_state = 'ending_orlov'
        st.rerun()

# Экран 7: Путь Потёмкина
elif st.session_state.game_state == 'potemkin_path':
    st.title("🏗️ Путь с Потёмкиным")

    col1, col2 = st.columns([1, 2])
    with col1:
        show_image(POTEMKIN_IMG, "Григорий Потёмкин")

    with col2:
        st.markdown("""
        **Потёмкин** изучает карты Новороссии:

        > *«Как освоить дикие степи? 
        > Военной силой... или хитростью?»*
        """)

    choice = st.radio("Твой ответ:", [
        "«Сила без ума груба, ум без силы бессилен»",
        "«Нужно строить города»",
        "«Это вопрос к Императрице»"
    ])

    if st.button("➡️ Продолжить"):
        st.session_state.stats['potemkin'] += 2
        st.session_state.stats['influence'] += 1
        st.session_state.game_state = 'ending_potemkin'
        st.rerun()

# Экран 8: Путь Зубова
elif st.session_state.game_state == 'zubov_path':
    st.title("💃 Путь с Зубовым")

    col1, col2 = st.columns([1, 2])
    with col1:
        show_image(ZUBOV_IMG, "Платон Зубов")

    with col2:
        st.markdown("""
        На балу **Платон Зубов** подходит к тебе:

        > *«Вы новенький? Как мило... 
        > При дворе так скучно без свежих лиц. 
        > Не составите компанию?»*
        """)

    choice = st.radio("Твой ответ:", [
        "«С удовольствием!»",
        "«Я здесь по делу»",
        "«Это вызовет слухи»"
    ])

    if st.button("➡️ Продолжить"):
        if "удовольствием" in choice:
            st.session_state.stats['zubov'] += 2
            st.session_state.game_state = 'ending_zubov'
        else:
            st.session_state.stats['influence'] += 1
            st.session_state.game_state = 'ending_neutral'
        st.rerun()

# === ФИНАЛЫ ===

elif st.session_state.game_state == 'ending_orlov':
    st.title("💕 ФИНАЛ: Любовь Орлова")
    show_image(ORLOV_IMG, "Григорий Орлов")
    st.markdown("""
    ## ❤️ Ты выбрал любовь!

    Ты стал доверенным лицом **Григория Орлова**. 
    Вместе вы участвуете в перевороте 1762 года.

    **Твоя награда:**
    -  Любовь героя России
    - 👑 Высокое положение при дворе
    - ⚡ Влияние на историю

    **Итог:** Романтическая победа! 🎉
    """)
    st.balloons()
    if st.button("🔄 Играть снова"):
        reset()
        st.rerun()

elif st.session_state.game_state == 'ending_potemkin':
    st.title("️ ФИНАЛ: Соратник Потёмкина")
    show_image(POTEMKIN_IMG, "Григорий Потёмкин")
    st.markdown("""
    ## 🏛️ Ты выбрал карьеру!

    Ты стал правой рукой **Потёмкина-Таврического**.
    Вместе вы осваиваете Новороссию и строите империю.

    **Твоя награда:**
    - 🏆 Государственные заслуги
    - 💰 Богатство и слава
    - 📚 Историческое наследие

    **Итог:** Политическая победа! 🎖️
    """)
    st.balloons()
    if st.button("🔄 Играть снова"):
        reset()
        st.rerun()

elif st.session_state.game_state == 'ending_zubov':
    st.title("💎 ФИНАЛ: Фаворит Зубова")
    show_image(ZUBOV_IMG, "Платон Зубов")
    st.markdown("""
    ## 💸 Ты выбрал роскошь!

    Ты стал близким другом **Платона Зубова**.
    Жизнь в роскоши, но... коррупция растёт.

    **Твоя награда:**
    - 💎 Богатство
    - 💃 Балы и развлечения
    - ⚠️ Но репутация под вопросом...

    **Итог:** Сомнительный выбор 😐
    """)
    if st.button("🔄 Играть снова"):
        reset()
        st.rerun()

elif st.session_state.game_state == 'ending_political':
    st.title("⚖️ ФИНАЛ: Независимый придворный")
    st.markdown("""
    ## 👑 Ты выбрал независимость!

    Ты не привязался ни к одному фавориту,
    но построил собственную карьеру.

    **Твоя награда:**
    - ⚡ Влияние при дворе
    - 🧠 Репутация мудреца
    - 🎯 Свобода выбора

    **Итог:** Стабильная карьера! ✨
    """)
    if st.button("🔄 Играть снова"):
        reset()
        st.rerun()

elif st.session_state.game_state == 'ending_neutral':
    st.title("📜 ФИНАЛ: Наблюдатель")
    st.markdown("""
    ## 🤔 Ты остался в стороне...

    Ты не рискнул сблизиться с фаворитами.
    Безопасно, но скучно.

    **Итог:** Попробуй ещё раз! 🔄
    """)
    if st.button("🔄 Играть снова"):
        reset()
        st.rerun()