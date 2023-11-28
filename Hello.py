import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():

    st.set_page_config(
        page_title="Marketing Events Tracker",
        page_icon="👋",
        layout="wide"
    )

    st.markdown("""
**👋 Hi! Sam here, co-founder at [MadKudu](https://www.madkudu.com).**</br>
This year, I’ve found tons of value in going to various marketing conferences and private events. But it was very hard to track what was happening, where, and when. I also missed out on a few cool small local events (FOMO!).</br>

I could not find a simple tracker of relevant events to consider, so here it goes.
                
Below a list of marketing events that you can filter in all kinds of ways: location, date, topics, main audience, price, etc.               

**⬇️ How to download this database?**</br>
Click “Download CSV” at the bottom-right of the sheet.

**🕵️‍♀️ See something missing/incorrect?**</br>
Send an email at sam+event@madkudu.com to recommend an event or to point to something incorrect.
                
**🙏 Credits**<br>
Contributors to the list: [Laura Hebert](https://www.linkedin.com/in/lauraehebert/), [Aline Romanelli](https://www.linkedin.com/in/aline-romanelli/), [Linh Ho](https://www.linkedin.com/in/linhho/), [Mark Kilens](https://www.linkedin.com/in/markkilens/)</br>
Inspiration: layoffs.fyi
                                                
    """, unsafe_allow_html=True)



    st.write("""<iframe class="airtable-embed" src="https://airtable.com/embed/appQZeUXGfZk6vItq/shrv9MXumkPs00nrH?backgroundColor=yellow&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="800" style="background: transparent; border: 1px solid #ccc;"></iframe>"""
             , unsafe_allow_html=True)


    hide_streamlit_style = """
                <style>
                [data-testid="stToolbar"] {visibility: hidden !important;}
                footer {visibility: hidden !important;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
