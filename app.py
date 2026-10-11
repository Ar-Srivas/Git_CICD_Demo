def predict_label(value):
    """Predict a label based on the input value."""
    return "positive" if value >= 0.5 else "negative"


if __name__ == "__main__":
    value = 0.8
    prediction = predict_label(value)
    print(f"Input value: {value}")
    print(f"Predicted label: {prediction}")
    print("Prediction completed successfully!")
