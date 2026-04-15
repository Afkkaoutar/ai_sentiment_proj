def detect_sentiment(message):
    negative_words = ["problème", "nul", "mauvais", "colère", "pas content"]
    positive_words = ["merci", "bien", "parfait", "satisfait", "excellent"]

    message = message.lower()

    for word in negative_words:
        if word in message:
            return "Négatif 😡"

    for word in positive_words:
        if word in message:
            return "Positif 😊"

    return "Neutre 😐"