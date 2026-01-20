import pandas as pd
import streamlit as st

@st.cache_data
def load_saved_tweets():
    """Load tweets from CSV file"""
    try:
        df = pd.read_csv('content/saved_tweets.csv')
        return df
    except FileNotFoundError:
        st.error("saved_tweets.csv not found in content folder")
        return None

def csv_to_tweet_dict(df, keyword=None, number=50):
    """Convert CSV dataframe to the format expected by app.py"""
    
    # Filter by keyword if provided
    if keyword:
        keyword_lower = keyword.lower().replace('#', '')
        df = df[df['text'].str.lower().str.contains(keyword_lower, na=False) | 
                df['topic'].str.lower().str.contains(keyword_lower, na=False)]
    
    # Limit number of tweets
    df = df.head(number)
    
    # Convert to the dict format that app.py expects
    tweets_list = []
    for _, row in df.iterrows():
        tweet = {
            "link": row['link'],
            "text": row['text'],
            "user": {
                "name": row['user']
            },
            "date": row['date'],
            "stats": {
                "comments": row['comments'],
                "retweets": row['retweets'],
                "quotes": row['quotes'],
                "likes": row['likes']
            }
        }
        tweets_list.append(tweet)
    
    return {"tweets": tweets_list, "meta": {"source": "CSV file"}}
