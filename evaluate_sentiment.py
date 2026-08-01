# evaluate_sentiment.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings("ignore")

# Download VADER lexicon
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Load the dataset (Tweets.csv must be in the same folder)
df = pd.read_csv("Tweets.csv")

print("Dataset loaded successfully!")
print("Total tweets:", len(df))
print("\nSentiment distribution:")
print(df['airline_sentiment'].value_counts())
print("-" * 50)

# Function to predict sentiment using VADER
def predict_sentiment(text):
    if not isinstance(text, str):
        return "neutral"
    
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"

print("Running sentiment analysis on the dataset... Please wait...")

# Apply prediction on all tweets
df['predicted_sentiment'] = df['text'].apply(predict_sentiment)

# True labels and predicted labels
y_true = df['airline_sentiment']
y_pred = df['predicted_sentiment']

# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)

print("\n" + "="*50)
print("EVALUATION RESULTS")
print("="*50)
print(f"Overall Accuracy: {accuracy * 100:.2f}%")

print("\nDetailed Classification Report:")
print(classification_report(y_true, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\n" + "="*50)
print("Sample Predictions:")
print("="*50)

sample = df[['text', 'airline_sentiment', 'predicted_sentiment']].sample(5, random_state=42)
for idx, row in sample.iterrows():
    print(f"\nText     : {row['text'][:90]}...")
    print(f"Actual   : {row['airline_sentiment']}")
    print(f"Predicted: {row['predicted_sentiment']}")