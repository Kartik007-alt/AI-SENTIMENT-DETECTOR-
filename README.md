<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis CLI Tool</title>
  
     
           
</head>
<body>

<div class="container">

<h1> Sentiment Analysis CLI Tool</h1>

<h2> Overview</h2>
<p>
The <b>Sentiment Analysis CLI Tool</b> is an AI-based application that analyzes text and classifies it into 
<b>Positive, Negative, or Neutral</b> sentiments. It uses <b>Natural Language Processing (NLP)</b> 
and <b>Machine Learning (Naive Bayes + TF-IDF)</b> for accurate predictions.
</p>

<h2> Features</h2>
<ul>
    <li>Real-time sentiment prediction</li>
    <li>CSV file sentiment analysis</li>
    <li>Machine Learning model training</li>
    <li>Accuracy calculation</li>
    <li>Confusion Matrix visualization</li>
    <li>Accuracy Graph</li>
    <li>Large dataset support (1000+ rows)</li>
    <li>Model saving and loading</li>
</ul>

<h2> Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Scikit-learn</li>
    <li>Pandas</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Joblib</li>
</ul>

<h2> Project Structure</h2>
<pre>
Sentiment-Analysis-CLI/
│-- advanced_sentiment_cli.py
│-- generate_dataset.py
│-- data.csv
│-- sentiment_model.pkl
│-- README.html
</pre>

<h2> Installation</h2>

<h3>1. Clone Repository</h3>
<pre>
git clone https://github.com/your-username/sentiment-cli.git
cd sentiment-cli
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install pandas scikit-learn matplotlib seaborn joblib
</pre>

<h2>How to Run</h2>

<h3>Generate Dataset</h3>
<pre>python generate_dataset.py</pre>

<h3>Run Application</h3>
<pre>python advanced_sentiment_cli.py</pre>

<h2> Usage</h2>
<pre>
1. Train Model
2. Predict Sentiment
3. Analyze CSV
4. Exit
</pre>

<h3>Example</h3>
<pre>
Input: I love this product
Output: POSITIVE
</pre>

<h2>Output</h2>
<ul>
    <li>Confusion Matrix</li>
    <li>Accuracy Graph</li>
</ul>

<h2> Model Details</h2>
<ul>
    <li>Algorithm: Naive Bayes</li>
    <li>Vectorization: TF-IDF</li>
    <li>Train/Test Split: 70/30</li>
</ul>

<h2> Applications</h2>
<ul>
    <li>Social media analysis</li>
    <li>Customer feedback analysis</li>
    <li>Product review classification</li>
    <li>Market research</li>
</ul>

<h2> Limitations</h2>
<ul>
    <li>Cannot detect sarcasm</li>
    <li>Depends on dataset quality</li>
</ul>

<h2> Future Enhancements</h2>
<ul>
    <li>Deep Learning models (LSTM, BERT)</li>
    <li>GUI version</li>
    <li>API integration</li>
</ul>

<h2> Author</h2>
<p>Your Name<br>Course: Fundamentals of AI & ML</p>

<h2> License</h2>
<p>For educational purposes only.</p>

</div>

</body>
</html>
