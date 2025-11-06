import ntscraper
import streamlit as st
import spacy

@st.cache_resource
def tweet_object(skip_check=False):
    
    # List of known working instances (as of late 2024)
    instances = [
        "https://nitter.poast.org",
        "https://nitter.privacydev.net",
        "https://nitter.net",
        "https://nitter.it"
    ]
    
    # Try each instance until one works
    for instance in instances:
        try:
            scraper = ntscraper.Nitter(
                instance=instance,
                skip_instance_check=True,
                log_level=0
            )
            st.success(f"✅ Connected to: {instance}")
            return scraper
        except Exception as e:
            st.warning(f"⚠️ Failed to connect to {instance}")
            continue
    
    # If all fail, try without specifying instance
    st.warning("All instances failed. Trying default configuration...")
    scraper = ntscraper.Nitter(skip_instance_check=False, log_level=1)
    return scraper



def fetch_tweets(keyword, mode, number, near=None, exclude=None, filters=None, to=None, language='en', since=None, until=None):
    from streamlit import error as st_error  # Optional if you want to display a nicer error

    scraper = tweet_object()
    tweet_dict = {"tweets": [], "meta": {}}  # default structure to avoid downstream crashes

    try:
        tweet_dict = scraper.get_tweets(
            keyword, mode=mode, number=number,
            near=near, exclude=exclude, filters=filters,
            to=to, language=language, since=since, until=until
        )
    except Exception as e:
        st.write("❗ Something went wrong while fetching tweets.")
        st_error(f"Error: {str(e)}")  # shows a collapsible error box
        print(f"[ERROR] fetch_tweets(): {e}")

    return tweet_dict

def get_location(tweet_text):
    
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(tweet_text)

    gpe_entities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    if gpe_entities:
        return ", ".join(gpe_entities)
    else:
        return "No location found"
