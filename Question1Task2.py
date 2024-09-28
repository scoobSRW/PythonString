import string

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

pos_keywords = ["good", "excellent"]
neg_keywords = ["bad", "poor"]


def counter(reviews):
    words = ' '.join(reviews).lower().translate(str.maketrans('', '', string.punctuation)).split()

    pos_count = sum(word in pos_keywords for word in words)
    neg_count = sum(word in neg_keywords for word in words)

    return pos_count, neg_count


if __name__ == "__main__":
    positive_count, negative_count = counter(reviews)
    print(f"Positive words count: {positive_count}")
    print(f"Negative words count: {negative_count}")