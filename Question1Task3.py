reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def summarize_reviews(reviews):
    summaries = []
    for review in reviews:
        if len(review) > 30:
            summary = review[:30].rsplit(' ', 1)[0] + '...'
        else:
            summary = review
        summaries.append(summary)
    return summaries

if __name__ == "__main__":
    review_summaries = summarize_reviews(reviews)
    print("Review Summaries:")
    for summary in review_summaries:
        print(summary)
