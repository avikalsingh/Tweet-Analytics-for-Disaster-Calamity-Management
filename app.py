import streamlit as st
from datetime import datetime
from scripts.classification_script import classify_tweets
from scripts.fetchtweets import fetch_tweets, get_location
from annotated_text import annotated_text

from scripts.embedtweet import Tweet
# t = Tweet("https://twitter.com/OReillyMedia/status/901048172738482176").component()   

st.set_page_config(page_title="Disaster Tweets Management",
                   page_icon="🕊️", layout="wide")

def main_page(input_dict):

    st.markdown("<center><h1>🕊️ Tweet Analytics for Disaster & Calamity Management</h1></center>", unsafe_allow_html=True)

    # alltabs, off_tab, on_tab = st.tabs(["All tweets", "On-topic", "Off-topic"])
    # ADD THIS INFO BANNER:
    st.info("""
    ℹ️ **Demo Mode**: This app currently uses pre-loaded tweet data due to Twitter/X discontinuing public access to Nitter instances.
    
    Available data: **200 #forestfire tweets** from December 2023.
    
    Live tweet fetching is temporarily unavailable.
    """)

    off_tweets = []
    on_tweets = []

    if input_dict:
        tweets_dict = fetch_tweets(**input_dict)

        # with alltabs:
        if tweets_dict["tweets"] != []:
            tweets = tweets_dict["tweets"]
            for tweet in tweets:
                loc_info = get_location(tweet["text"])

                with st.container(border=True):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.subheader("User")
                        st.write(tweet["user"]["name"])
                        # classif = classify_tweets(tweet["text"])
                        # if classif["status"] == "On-topic":
                        #     annotated_text((classif["status"], str(classif["conf"]), "#4DD0E1"))
                        #     on_tweets.append([tweet, classif, loc_info])
                        # else:
                        #     annotated_text((classif["status"], str(classif["conf"]), "#BF565A"))
                        #     off_tweets.append([tweet, classif, loc_info])

                        annotated_text((loc_info, "", "#50C878"))

                    with col2:
                        st.subheader("Tweet")
                        st.write(tweet["text"])

                    with col3:
                        st.subheader("Link")
                        st.write(tweet["link"])
        else:
            st.write("Empty list returned, change parameters and retry")
        
        # with offtab:
        # with ontab:


def sidebar_page():
    # with st.sidebar:
    #     st.title("Fetch Tweets")
        
    #     # Add CSV demo mode option
    #     use_csv = st.checkbox("📁 Use saved tweets (Demo Mode)", value=True)
        
    #     if use_csv:
    #         st.info("Using pre-loaded forest fire tweets from CSV")
    #         keyword = st.selectbox("Select topic", ["forestfire", "earthquake", "floods", "hurricane"])
    #         mode = "hashtag"
    #         number = st.slider("Number of tweets", 10, 200, 50)
    #         location = None
    #         user_mention = None
    #     else:
    #         # Your existing code for live fetching
    #         keyword = st.text_input("Tweets from User, Hashtag, Term")
    #         mode = st.selectbox("Select the type of keyword", options=["keyword", "hashtag", "user"], index=1,
    #                             format_func = lambda x: "term" if x == "keyword" else x)
    #         number = st.number_input("Number of tweets to fetch", min_value=10, max_value=100)
    #         location = st.text_input("Location of the tweet")
    #         user_mention = st.text_input("User Mentions (if any)")
        
    #     btn = st.button("Search")
        
    #     if btn and keyword != "" and number != None:
    #         if location == "": location = None
    #         if user_mention == "": user_mention = None
    #         if mode == "keyword": mode = "term"
            
    #         return {"keyword": keyword, "number": number, "mode": mode, "near": location,
    #                 "since": None, "until": None, "to": user_mention}
    with st.sidebar:
        st.title("📁 Saved Tweet Dataset")
        
        st.caption("Due to Twitter/X restrictions, live fetching is unavailable. Using saved dataset.")
        
        keyword = st.selectbox(
            "Select disaster type:",
            ["forestfire"],
            help="Only forest fire tweets available in demo"
        )
        
        mode = "hashtag"
        
        number = st.slider(
            "Number of tweets to display:", 
            min_value=10, 
            max_value=200, 
            value=50,
            step=10
        )
        
        btn = st.button("Load Tweets", type="primary")
        
        if btn:
            return {
                "keyword": keyword, 
                "number": number, 
                "mode": mode, 
                "near": None,
                "since": None, 
                "until": None, 
                "to": None
            }

        



if __name__ == "__main__":

    input_dict = sidebar_page()

    if input_dict != {} or input_dict != None:
        main_page(input_dict)