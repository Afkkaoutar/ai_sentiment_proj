from sentiment import detect_sentiment
from utils import get_priority, suggest_response, satisfaction_score
from storage import save_to_file, load_data, log_action

history = load_data()


def show_menu():
    print("\n==============================")
    print("   AI SENTIMENT ANALYZER")
    print("==============================")
    print("1. Analyser un message")
    print("2. Voir l'historique")
    print("3. Voir les statistiques")
    print("4. Générer un rapport")
    print("5. Quitter")


def analyze_message():
    message = input("\n📝 Entrez un message client: ")

    result = detect_sentiment(message)
    priority = get_priority(result)
    response = suggest_response(result)

    history.append((message, result))

    save_to_file(message, result)
    log_action(f"ANALYZE | {message} | {result}")

    print("\n=== RESULTAT ===")
    print("Sentiment :", result)
    print("Priorité :", priority)
    print("Réponse suggérée :", response)


def show_history():
    print("\n=== HISTORIQUE ===")

    if not history:
        print("Aucune donnée.")
        return

    for i, (msg, res) in enumerate(history, 1):
        print(f"{i}. {msg} --> {res}")


def show_stats():
    print("\n=== STATISTIQUES ===")

    if not history:
        print("Aucune donnée.")
        return

    positive = sum(1 for _, r in history if "Positif" in r)
    negative = sum(1 for _, r in history if "Négatif" in r)
    neutral = sum(1 for _, r in history if "Neutre" in r)

    score = satisfaction_score(history)

    print(f"Total messages : {len(history)}")
    print(f"Positifs 😊 : {positive}")
    print(f"Négatifs 😡 : {negative}")
    print(f"Neutres 😐 : {neutral}")
    print(f"Satisfaction globale : {score:.2f}%")


def generate_report():
    print("\n=== RAPPORT COMPLET ===")

    total = len(history)
    if total == 0:
        print("Aucune donnée.")
        return

    positive = sum(1 for _, r in history if "Positif" in r)
    negative = sum(1 for _, r in history if "Négatif" in r)
    neutral = sum(1 for _, r in history if "Neutre" in r)

    report = f"""
📊 RAPPORT SYSTEME
------------------------
Total messages : {total}
Positifs : {positive}
Négatifs : {negative}
Neutres : {neutral}
Taux satisfaction : {(positive/total)*100:.2f}%
------------------------
"""

    print(report)

    log_action("REPORT GENERATED")


def main():
    while True:
        show_menu()
        choice = input("\n👉 Choisissez une option: ")

        if choice == "1":
            analyze_message()
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("👋 Au revoir")
            break
        else:
            print("❌ Option invalide")


if __name__ == "__main__":
    main()