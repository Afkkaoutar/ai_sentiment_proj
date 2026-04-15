def generate_report(history):
    total = len(history)

    positive = sum(1 for _, r in history if "Positif" in r)
    negative = sum(1 for _, r in history if "Négatif" in r)
    neutral = sum(1 for _, r in history if "Neutre" in r)

    report = f"""
=== RAPPORT ===
Total messages : {total}
Positifs : {positive}
Négatifs : {negative}
Neutres : {neutral}
"""

    return report