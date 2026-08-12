# 🎯 Internship Task #1 — Sentiment-Aware Customer Support Chatbot

## 📌 Project Overview

This project is **Internship Task #1** completed as an extension of the **Real-Time Gen-AI Customer Support Chatbot** developed during the Elevance Skills training program.

The objective of this internship task is to integrate **sentiment analysis** into a customer-support chatbot so that the system can understand the sentiment expressed in customer messages and respond appropriately.

Customer-support conversations are not always neutral. Users may express satisfaction, frustration, anger, appreciation, or simply ask factual questions. A chatbot that understands the sentiment of a message can provide responses that are more appropriate to the customer's situation.

This implementation classifies customer messages into three sentiment categories:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

The detected sentiment is then used to influence the chatbot's response.

---

# 🔗 Connection to the Training Project

### Original Training Project

**Real-Time Gen-AI Customer Support Chatbot**

The training project focused on developing a chatbot capable of interacting with users in a customer-support environment using Generative AI.

### Internship Extension

**Task #1 — Sentiment Analysis**

This internship task builds on the same customer-support chatbot concept by introducing a sentiment-analysis component.

The extension allows the chatbot to identify the emotional direction of a customer's message and adapt its response accordingly.

```text
                    TRAINING PROJECT
                          │
                          ▼
          Real-Time Gen-AI Customer Support
                    Chatbot
                          │
                          ▼
                  INTERNSHIP TASK #1
                          │
                          ▼
                 Sentiment Analysis
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
           Positive    Neutral     Negative
              │           │           │
              └───────────┼───────────┘
                          ▼
                Appropriate Response
