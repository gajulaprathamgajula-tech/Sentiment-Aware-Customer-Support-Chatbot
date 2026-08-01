# Sentiment-Aware Customer Support Chatbot

A smart customer support chatbot that can detect the emotional tone of user messages (Positive, Negative, or Neutral) and respond in a more human and appropriate way.

This project was developed as part of an internship to integrate **Sentiment Analysis** into a customer support chatbot.

---

## Project Description

Traditional chatbots reply with fixed responses and do not understand how the customer is feeling.  
This project solves that problem by adding **Sentiment Analysis**.

The chatbot analyzes every user message using **VADER (Valence Aware Dictionary and sEntiment Reasoner)** and then generates a suitable reply based on the detected emotion.

### Key Capabilities:
- Detects Positive, Negative, and Neutral sentiments
- Gives empathetic replies when the user is angry or frustrated
- Gives friendly replies when the user is happy
- Handles common customer support queries such as:
  - Order tracking
  - Refund requests
  - Product complaints
  - General help

---

## Features

- Real-time sentiment detection
- Emotion-aware response generation
- Simple console-based chatbot interface
- Evaluation on a real-world dataset
- Easy to run and understand

---

## Dataset Used

**Twitter US Airline Sentiment Dataset** (from Kaggle)

- Total tweets: **14,640**
- Sentiment labels: Positive, Negative, Neutral
- Source: [Kaggle - Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

This dataset contains real customer tweets about airlines. It was used to evaluate how accurately the sentiment analysis model works.

### Evaluation Result:
- Overall Accuracy: **≈ 65%**

---

## Technologies Used

| Technology       | Purpose                              |
|------------------|--------------------------------------|
| Python           | Main programming language            |
| NLTK (VADER)     | Sentiment Analysis                   |
| Pandas           | Dataset handling                     |
| Scikit-learn     | Accuracy calculation & evaluation    |

---

## Project Structure
