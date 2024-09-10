from flask import Flask, request, render_template, redirect, send_from_directory
import os

# Flask uygulamasını oluştur
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

posts = [
    {
        "id": 1,
        "title": "Focus on Zero Trust",
        "content": "The Zero Trust model emphasizes continuous verification for every request, regardless of its origin. This approach enhances security by ensuring that no request is implicitly trusted.",
        "comments": []
    },
    {
        "id": 2,
        "title": "Post Başlığı 2",
        "content": "Bu başka bir post örneğidir.",
        "comments": []
    }
]

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if request.method == 'POST':
        comment = request.form.get('comment', '')
        post['comments'].append(comment)
    return render_template('post.html', post=post)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    return f'Arama Sonuçları: {query}'

if __name__ == '__main__':
    app.run(debug=True)
