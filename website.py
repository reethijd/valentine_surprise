import streamlit as st
import base64

st.set_page_config(page_title="Valentine Website 💖", page_icon="💘")

# --- Initialize session state ---
if "welcome_clicked" not in st.session_state:
    st.session_state.welcome_clicked = False

if "message_opened" not in st.session_state:
    st.session_state.message_opened = False

# Banner Image
st.image("draw-vector-illustration-character-design-260nw-2092357630.webp", width=700)

# --- STEP 1 Button (WELCOME) ---
if not st.session_state.welcome_clicked:
    if st.button("#### 💖 Welcome to my Valentine surprise website 🌹"):
        st.session_state.welcome_clicked = True

# --- After Welcome Clicked (SHOW AUDIO + GIF) ---
if st.session_state.welcome_clicked:

    st.markdown("### 🎵 Just feel the song...")

    # Audio
    audio_file = open("_Jodi_Nilave_.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

    # Animated GIF
    file_ = open("valentinenwen-12.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/gif;base64,{data_url}" width="600">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # --- STEP 2 Button (MESSAGE BUTTON) ---
    if not st.session_state.message_opened:
        if st.button("💌 Click here to open my personal message"):
            st.session_state.message_opened = True

# --- After Message Button Clicked (SHOW MESSAGE) ---
if st.session_state.message_opened:

    st.markdown(
        """

        ### Dear Suganth  💌,

        You are the one I believed in and loved with my whole heart.  
        You showed me what eternal love truly means, and you have given me everything I ever wished for.

        I know this must be such a surprise for you… you definitely didn’t expect this 😂💖  
        And honestly, it’s beyond your imagination too.  
        I just hope you love it as much as I loved creating it for you.

        I want to travel through this entire life with you —  
        holding your hand through every moment, every happiness, and every storm.  
        No matter what the situation is, I will always be there for you.

        Let’s stay together and create a beautiful life journey…  
        a love so pure that it brings happy tears to those who witness it.

        I love you so much, until my very last breath.  
        You are the man I have always dreamed of.  
        You gave me freedom, care, respect, and the kind of love I never knew I needed.

        I love you endlessly, babz ❤️🌹  

        ### Happy Valentine’s Day, my love 💘  
        """
    )

    st.markdown("### 💖💘💝💞💓💗❤️💘💖")







