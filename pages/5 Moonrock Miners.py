import streamlit as st
from common_config import common_config, back_to_home, back_to_menu

common_config()

try:
    if st.session_state.game != "MoonrockMiners":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "MoonrockMiners"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "MoonrockMiners" and st.session_state.page == "menu":
    with ph.container():
        st.html(
            """<style>
                    div[data-testid="column"] {
                        width: fit-content !important;
                        flex: unset;
                    }
                    div[data-testid="column"] * {
                        width: fit-content !important;
                    }
                    div[data-testid="stVerticalBlock"] p::before {
                        display: inline-block;
                        vertical-align: middle;
                        font-weight: 900;
                        font-size: 20px;
                        color: white;
                        padding-right: 5px;
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(6) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Free" !important;
                        content: "\\f0ac";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(8) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f392";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(11) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.image("static/moonrock_miners_banner.png", width=500)
        st.markdown(
            """**Moonrock Miners** is a gravity-defying multiplayer space battle game set in an asteroid field. Blast other players, collect powerups and crystals, and avoid the asteroids. Try to survive until the end to win the match. Compete against players around the world in real-time to rank in every season. You can also create your own custom lobbies to play private games online with your friends!"""
        )
        st.info(
            "**Moonrock Miners** is **no longer in development**",
            icon="ℹ️",
        )
        st.html("<h4>Platform</h4>")
        col1, col2 = st.columns(2)
        col1.link_button("Browser", "https://moonrockminers.com")
        st.html("<h4>Community</h4>")
        col1, col2 = st.columns(2)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        "---"
        st.html("<h3><i class='fa-solid fa-chart-simple'></i>&nbsp;Statistics</h3>")
        col1, col2 = st.columns(2)
        col1.button(
            "Season Leaderboard (WIP)",
            on_click=to_season_leaderboard_page,
            type="primary",
        )
        st.info(
            "**Leaderboard** is **disabled** currently",
            icon="ℹ️",
        )
        back_to_home()

elif (
    st.session_state.game == "MoonrockMiners"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from pages.MoonrockMiners.Statistics.season_leaderboard import (
            load_page as MoonrockMiners_season_leaderboard,
        )

        MoonrockMiners_season_leaderboard()
        back_to_menu()