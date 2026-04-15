from sentiment import detect_sentiment

def analyze_batch(messages):
    results = []

    for msg in messages:
        result = detect_sentiment(msg)
        results.append((msg, result))

    return results