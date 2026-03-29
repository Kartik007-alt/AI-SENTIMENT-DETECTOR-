import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

import pandas as pd
import os
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer


MODEL_FILE = "sentiment_model.pkl"


# Load Model

def load_model():
    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)
    return None



# Train Model

def train_model():
    if not os.path.exists("data.csv"):
        print(" data.csv not found!")
        return None

    data = pd.read_csv("data.csv")

    X = data["text"]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=42
    )

    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, MODEL_FILE)

    print(f"\n Model trained successfully!")
    print(f" Accuracy: {accuracy * 100:.2f}%")

    
    # Confusion Matrix
    
    cm = confusion_matrix(y_test, predictions, labels=["positive", "negative", "neutral"])

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d',
                xticklabels=["positive", "negative", "neutral"],
                yticklabels=["positive", "negative", "neutral"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    
    #  Accuracy Graph (Simple)
    
    plt.figure()
    plt.bar(["Accuracy"], [accuracy])
    plt.title("Model Accuracy")
    plt.ylabel("Score")
    plt.show()

    return model




# Predict Sentiment

def predict_sentiment(model):
    text = input("\nEnter text: ")

    if not text.strip():
        print(" Empty input!")
        return

    prediction = model.predict([text])[0]
    print(f" Sentiment: {prediction.upper()}")



# Analyze CSV File

def analyze_csv(model):
    file_name = input("Enter CSV file name: ")

    if not os.path.exists(file_name):
        print(" File not found!")
        return

    data = pd.read_csv(file_name)

    if "text" not in data.columns:
        print(" CSV must contain 'text' column!")
        return

    data["predicted_sentiment"] = model.predict(data["text"])

    output_file = "output_" + file_name
    data.to_csv(output_file, index=False)

    print(f" Analysis complete. Saved as {output_file}")



# Menu

def menu():
    print("\n===== Advanced Sentiment Analysis CLI =====")
    print("1. Train Model")
    print("2. Predict Sentiment (Single Input)")
    print("3. Analyze CSV File")
    print("4. Exit")



# Main Program

def main():
    model = load_model()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            model = train_model()

        elif choice == '2':
            predict_sentiment(model)

        elif choice == '3':
            analyze_csv(model)

        elif choice == '4':
            print(" Exiting...")
            break

        else:
            print(" Invalid choice")


if __name__ == "__main__":
    main()


