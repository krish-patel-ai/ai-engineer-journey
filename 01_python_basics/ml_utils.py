def calculate_accuracy(correct, total):
    if total == 0:
        return 0
    return correct / total


def classify_loss(loss):
    if loss < 0.3:
        return "Low"
    elif loss < 0.7:
        return "Medium"
    else:
        return "High"


VERSION = "1.0"