def predict_label(value):
    """Predict a label based on the input value."""
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")

    if not 0 <= value <= 1:
        raise ValueError("Input must be between 0 and 1")

    return "positive" if value >= 0.5 else "negative"


if __name__ == "__main__":
    value = 0.8
    prediction = predict_label(value)

    print("MLOps Prediction Demo")
    print("---------------------")
    print(f"Input value: {value}")
    print(f"Predicted label: {prediction}")
    print("Prediction completed successfully!")