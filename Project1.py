import streamlit as st
import random
import json
import os

# ------------------ Title ------------------
st.set_page_config(page_title="Mood Music Recommender", page_icon="🎧")
st.title("🎧 Mood-Based Music Recommender")

# ------------------ Data ------------------
mood_music = {
    "Happy": [
        {"song": "Tere Liye", 
         "image": "Images-Python/Tere liye.png",
         "audio": "Audio-Python/tere liye.mp3"},
        
        {"song": "Chori choriye", 
         "image": "Images-Python/chori choriye.jpg",
         "audio": "Audio-Python/chori choriye.mp3"},
        
        {"song": "Happier", 
         "image": "Images-Python/happier.jpg",
         "audio": "Audio-Python/happier.mp3"},
        
        {"song": "Ye Ishq hai", 
         "image": "Images-Python/yeh ishq hai.jpg",
         "audio": "Audio-Python/Ye Ishq Hai.mp3"},
        
        {"song": "Hrudayam Ekkadunnadi", 
         "image": "Images-Python/hrudayam ekkadunnadi.jpg",
         "audio": "Audio-Python/Hrudayam Ekkadunnadi.mp3"},
        
        {"song": "Choolenge Aasma", 
         "image": "Images-Python/choolenge aasma.jpg",
         "audio": "Audio-Python/Choolenge Aasma.mp3"}
    ],
    
    "Sad": [
        {"song": "Channa Mereya", 
         "image": "Images-Python/channa mereya.jpg",
         "audio": "Audio-Python/channa mereya.mp3"},
        
        {"song": "Atu Nuvve", 
         "image": "Images-Python/atu nuvve.jpg",
         "audio": "Audio-Python/atu nuvve.mp3"},
        
        {"song": "Arz kiya hai", 
         "image": "Images-Python/arz kiya hai.jpg",
         "audio": "Audio-Python/arz kiya hai.mp3"},
        
        {"song": "Ve kamleya", 
         "image": "Images-Python/ve kamleya.jpg",
         "audio": "Audio-Python/ve kamleya.mp3"},
        
        {"song": "Vurike Chilaka", 
         "image": "Images-Python/vurike chilaka.jpg",
         "audio": "Audio-Python/vurike chilaka.mp3"},
        
        {"song": "Kabira", 
         "image": "Images-Python/kabira.jpg",
         "audio": "Audio-Python/kabira.mp3"},
        
        {"song": "Earthquake",  
         "image": "Images-Python/earthquake.jpg",
         "audio": "Audio-Python/earthquake.mp3"}
    ],
    
    "Feeling Low":[
        {"song": "Pal Pal dil ke paas",  
         "image": "Images-Python/pal pal dil ke paas",
         "audio": "Audio-Python/pal pal dil ke paas.mp3"},
        
        {"song": "Naa Pranam", 
         "image": "Images-Python/naa pranam.jpg",
         "audio": "Audio-Python/naa pranam.mp3"},
        
        {"song": "Finding Her", 
         "image": "Images-Python/finding her.jpg",
         "audio": "Audio-Python/finding her.mp3"},
        
        {"song": "Gira gira gira", 
         "image": "Images-Python/gira gira gira.jpg",
         "audio": "Audio-Python/gira gira gira.mp3"}, 
    ],
       
    "Motivated":[
        {"song": "Hall of fame", 
         "image": "Images-Python/hall of fame.jpg",
         "audio": "Audio-Python/hall of fame.mp3"},
        
        {"song": "Mari Antaga", 
         "image": "Images-Python/mari antaga.jpg",
         "audio": "Audio-Python/mari antaga.mp3"},
        
        {"song": "Nee Prashnalu", 
         "image": "Images-Python/nee prashnalu.jpg",
         "audio": "Audio-Python/nee prashnalu.mp3"},
        
        {"song": "Believer", 
         "image": "Images-Python/believer.jpg",
         "audio": "Audio-Python/believer.mp3"},
        
        {"song": "Nuvvani Idi Nenani", 
         "image": "Images-Python/maharshi.jpg",
         "audio": "Audio-Python/maharshi.mp3"}
    ],
        
    "Romantic": [
        {"song": "Tum hi ho", 
         "image": "Images-Python/tum hi ho.jpg",
         "audio": "Audio-Python/tum hi ho.mp3"},
        
        {"song": "Gulabi Kallu Rendu", 
         "image": "Images-Python/gulabi kallu rendu.jpg",
         "audio": "Audio-Python/gulabi kallu rendu.mp3"},
        
        {"song": "Beautiful Love", 
         "image": "Images-Python/beautiful love.jpg",
         "audio": "Audio-Python/beautiful love.mp3"},
        
        {"song": "Ammayi", 
         "image": "Images-Python/ammayi.jpg",
         "audio": "Audio-Python/ammayi.mp3"},
        
        {"song": "Prema Swaramulalo", 
         "image": "Images-Python/prema swaramulalo.jpg",
         "audio": "Audio-Python/prema swaramulalo.mp3"},
        
        {"song": "Violin Song", 
         "image": "Images-Python/violin.jpg",
         "audio": "Audio-Python/violin song.mp3"},
        
        {"song": "kanulanu Thaake", 
         "image": "Images-Python/kanulanu thaake.jpg",
         "audio": "Audio-Python/kanulanu thaake.mp3"}
    ],
    
    "Party" : [
        {"song": "Kala Chashma", 
         "image": "Images-Python/kala chashma.jpg",
         "audio": "Audio-Python/kala chashma.mp3"},
        
        {"song": "Nanu Gelichey Magavadu", 
         "image": "Images-Python/nanu geliche magavadu.jpg",
         "audio": "Audio-Python/nanu geliche magavadu.mp3"},
        
        {"song": "Aavan Jaavan", 
         "image": "Images-Python/aavan jaavan.jpg",
         "audio": "Audio-Python/aavan jaavan.mp3"},
        
        {"song": "Choti Choti Baatein", 
         "image": "Images-Python/choti choti batein.jpg",
         "audio": "Audio-Python/choti choti baatein.mp3"},
        
        {"song": "Ek ho gaye hum aur tum", 
         "image": "Images-Python/bombay.jpg",
         "audio": "Audio-Python/humma humma.mp3"}
    ],
    
    "Mass Beat" : [
        {"song": "Jorse Jorse", 
         "image": "Images-Python/jorse jorse.jpg",
         "audio": "Audio-Python/jorse jorse.mp3"},
        
        {"song": "Door Number Okati", 
         "image": "Images-Python/Oopiri.jpg",
         "audio": "Audio-Python/door number.mp3"},
        
        {"song": "Pavazha malli", 
         "image": "Images-Python/pavazha malli.jpg",
         "audio": "Audio-Python/pavazha malli.mp3"},
        
        {"song": "Chikni Chameli", 
         "image": "Images-Python/chikni chameli.jpg",
         "audio": "Audio-Python/chikni chameli.mp3"},
        
        {"song": "Naa Pere Kaanchanamaala", 
         "image": "Images-Python/mbbs.jpg",
         "audio": "Audio-Python/naa pere kaanchanmala.mp3"}
    ],
    
    "Pleasant": [
        {"song": "Kallu Moosi Yochisthey", 
         "image": "Images-Python/kallu moosi.jpg",
         "audio": "Audio-Python/kallu moosi yochistey.mp3"},
        
        {"song": "Zaalima", 
         "image": "Images-Python/zaalima.jpg",
         "audio": "Audio-Python/zaalima.mp3"},
        
        {"song": "Tere Hawaale", 
         "image": "Images-Python/tere hawaale.jpg",
         "audio": "Audio-Python/tere hawaale.mp3"},
        
        {"song": "Die with a smile", 
         "image": "Images-Python/die with a smile.jpg",
         "audio": "Audio-Python/die with a smile.mp3"},
        
        {"song": "O Cheliya", 
         "image": "Images-Python/o cheliya.jpg",
         "audio": "Audio-Python/o cheliya.mp3"},
        
        {"song": "Oonchi Oonchi Deewarein", 
         "image": "Images-Python/oonchi oonchi.jpg",
         "audio": "Audio-Python/oonchi oonchi deewarein.mp3"}
    ],
    
    "BGM" : [
        {"song": "Naagin3", 
         "image": "Images-Python/naagin.jpg",
         "audio": "Audio-Python/naagin3_BGM.mp3"},
        
        {"song": "yenthavadu gani", 
         "image": "Images-Python/Yentha vadu gani.jpg",
         "audio": "Audio-Python/Enthavadugani_BGM.mp3"},
        
        {"song": "Engagement Ring", 
         "image": "Images-Python/remo.jpg",
         "audio": "Audio-Python/remo_BGM.mp3"},
        
        {"song": "Animal ", 
         "image": "Images-Python/animal.jpg",
         "audio": "Audio-Python/Animal_BGM.mp3"},
        
        {"song": "Aashiqui", 
         "image": "Images-Python/aashiqui bgm",
         "audio": "Audio-Python/Aashiqui_BGM.mp3"}
    ]
}

# ------------------ History File ------------------
HISTORY_FILE = "history.json"

# Create file if not exists
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

# ------------------ Functions ------------------

def save_history(song):
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    
    data.append(song)
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f)


def show_history():
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    
    if len(data) == 0:
        st.info("No history yet!")
    else:
        st.subheader("📜 Recommendation History")
        for i, song in enumerate(data, 1):
            st.write(f"{i}. {song}")


def clear_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)
    st.success("History cleared!")

# ------------------ UI ------------------

menu = st.sidebar.selectbox("Menu", ["Home", "History", "Clear History"])

if menu == "Home":
    st.subheader("Select Your Mood 🎭")
    
    mood = st.selectbox("Choose mood", list(mood_music.keys()))
    
    if st.button("🎶 Recommend Song"):
        song_data = random.choice(mood_music[mood])
        
        st.success(f"🎵 {song_data['song']}")
        
        # Show image
        if os.path.exists(song_data["image"]):
            st.image(song_data["image"], width=300)
        else:
            st.error("Image not found!")
        
        # 🔥 PLAY AUDIO
        if os.path.exists(song_data["audio"]):
            with open(song_data["audio"], "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
        else:
            st.error("Audio file not found!")
        
        save_history(song_data["song"])
        st.balloons()

elif menu == "History":
    show_history()

elif menu == "Clear History":
    clear_history()