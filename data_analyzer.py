def analyze_data(numbers):
    """Return basic statistics for a list of numbers."""
    if not numbers:
        return {"count": 0, "total": 0, "average": 0}

    total = sum(numbers)
    average = total / len(numbers)

    return {
        "count": len(numbers),
        "total": total,
        "average": round(average, 2)
    }


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]

    results = analyze_data(data)

    print("Data Analysis")
    print("-------------")
    print(f"Count: {results['count']}")
    print(f"Total: {results['total']}")
    print(f"Average: {results['average']}")
