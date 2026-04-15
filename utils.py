def get_priority(sentiment):
    if "Négatif" in sentiment:
        return "Haute priorité 🚨"
    elif "Neutre" in sentiment:
        return "Priorité moyenne ⚠️"
    else:
        return "Basse priorité ✅"


def suggest_response(sentiment):
    if "Négatif" in sentiment:
        return "Nous sommes désolés pour ce problème, nous allons vous aider rapidement."
    elif "Positif" in sentiment:
        return "Merci pour votre retour positif ! 😊"
    else:
        return "Merci pour votre message, nous restons à votre disposition."


def satisfaction_score(history):
    total = len(history)
    if total == 0:
        return 0

    positive = sum(1 for _, r in history if "Positif" in r)
    return (positive / total) * 100