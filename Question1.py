reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "bad", "excellent", "poor", "average"]

def highlighter(reviews, keywords):
    updated_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        updated_reviews.append(review)
    return updated_reviews

if __name__ == "__main__":
    capitalized_reviews = highlighter(reviews, keywords)
    print("Capitalized Reviews:")
    for review in capitalized_reviews:
        print(review)
