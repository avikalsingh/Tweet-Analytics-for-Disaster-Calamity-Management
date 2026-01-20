# Tweet Analytics for Disaster & Calamity Management

A Streamlit-based application for analyzing and classifying disaster-related tweets to support situational awareness and emergency response research.

> **Note:** Due to Twitter/X restrictions, live tweet fetching is currently unavailable.  
> This application runs in **demo mode** using a curated dataset of disaster-related tweets.

---

## Problem Statement

During natural disasters, social media platforms generate large volumes of real-time information. However, this data is noisy, unstructured, and difficult to operationalize quickly.

This project demonstrates how Natural Language Processing (NLP) and machine learning can be used to **identify relevant disaster-related tweets** and extract **actionable signals** for monitoring and response.

---

## Key Features

- Streamlit-based interactive web application
- NLP pipeline for tweet preprocessing and embedding
- Machine-learning–based classification of disaster relevance
- Named Entity Recognition (NER) for extracting location information
- Demo dataset fallback to ensure reproducibility and deployability

---

## Application Mode

- **Demo Mode (Current)**
  - Uses a preloaded dataset of disaster-related tweets
  - Designed to showcase the end-to-end analytics and classification pipeline

- **Live Fetching**
  - Temporarily disabled due to Twitter/X API and Nitter access limitations

---

## Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- Pandas, NumPy  
- spaCy (NER)  
- ntscraper (historical / deprecated live fetching)  

---

## Repository Structure

```text
.
├── app.py                  # Streamlit entry point
├── scripts/                # Data processing & ML pipeline
├── content/                 # Demo datasets (sanitized)
├── requirements.txt
├── README.md

```
---
## Repository Structure
pip install -r requirements.txt

streamlit run app.py


---
## Disclaimer

This project is intended for educational and research purposes.

No private or sensitive user data is collected or stored.

---


