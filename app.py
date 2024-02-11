from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment_label(polarity):
    print(polarity)
    polarity = round(polarity, 1)
    print(polarity)

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    message = request.json["message"]
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity
    sentiment = get_sentiment_label(polarity)
    return jsonify({"sentiment": sentiment})

@app.route("/result")
def result():
    # Get the sentiment from the query parameter
    sentiment = request.args.get("sentiment")
    return render_template("result.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
