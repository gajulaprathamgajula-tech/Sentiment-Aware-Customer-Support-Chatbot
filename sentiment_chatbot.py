# sentiment_chatbot.py

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> dict:
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "compound": compound,
        "scores": scores
    }


def generate_response(user_message: str, sentiment: dict) -> str:
    label = sentiment["label"]
    compound = sentiment["compound"]
    msg = user_message.lower().strip()

    if any(word in msg for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "Hello! Welcome to customer support. How can I help you today?"

    if any(word in msg for word in ["thank", "thanks", "thank you"]):
        return "You're most welcome! Is there anything else I can help you with?"

    if any(word in msg for word in ["order", "track", "tracking", "delivery", "shipping", "where is my"]):
        if label == "negative":
            return "I'm sorry for the delay or issue with your order. Could you please share your Order ID? I'll check it right away."
        else:
            return "Sure! I can help you track your order. Please share your Order ID."

    if any(word in msg for word in ["refund", "return", "money back", "cancel order"]):
        if label == "negative":
            return "I'm really sorry you had a bad experience. I can help you with a refund or return. Please share your Order ID and the reason."
        else:
            return "Of course. I can assist you with a refund or return. Could you please provide your Order ID?"

    if any(word in msg for word in ["broken", "damaged", "not working", "defective", "poor quality", "bad product"]):
        return "I'm very sorry to hear that the product has an issue. Please share your Order ID and a short description of the problem so I can help you quickly."

    if label == "negative" and compound < -0.4:
        return "I sincerely apologize for the trouble you're facing. Your concern is important to us. Please tell me more details so I can resolve this for you."

    if label == "positive" and compound > 0.5:
        return "Thank you so much for the kind words! We're really happy you're satisfied. Is there anything else I can do for you?"

    if any(word in msg for word in ["help", "support", "assist", "problem", "issue"]):
        if label == "negative":
            return "I'm here to help you. Please tell me exactly what problem you're facing so I can assist you better."
        else:
            return "Of course, I'm here to help! What do you need assistance with?"

    if label == "positive":
        return "That's nice to hear! How else can I assist you today?"
    elif label == "negative":
        return "I'm sorry you're not happy with this. Please share more details so I can help fix it."
    else:
        return "Got it. Could you please tell me a bit more so I can help you better?"


def chatbot():
    print("=" * 60)
    print("   Smart Customer Support Bot + Sentiment Analysis")
    print("=" * 60)
    print("Type your message (or 'quit' / 'exit' to stop)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nBot: Thank you for contacting us. Have a great day!")
            break

        if not user_input:
            continue

        sentiment = analyze_sentiment(user_input)
        response = generate_response(user_input, sentiment)

        print(f"[Detected: {sentiment['label'].upper()} | Score: {sentiment['compound']:.3f}]")
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chatbot()