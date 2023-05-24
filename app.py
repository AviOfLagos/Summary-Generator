import openai

app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-summary', methods=['POST'])
def generate_summary():
    job_title = request.form['jobTitle']
    company = request.form['company']
    skills = request.form['skills']
    goals = request.form['goals']
    platforms = request.form.getlist('platforms')

    # Generate summary using OpenAI's GPT-4
    prompt = f"I am a {job_title} at {company}. I have {skills}. My goals are {goals}."
    response = openai.Completion.create(
        engine='text-davinci-004',
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1
    )
    summary = response.choices[0].text.strip()

    # Perform keyword optimization based on platforms
    if 'LinkedIn' in platforms:
        summary += " #LinkedIn"
    if 'Twitter' in platforms:
        summary += " #Twitter"
    if 'Resume' in platforms:
        summary += " #Resume"

    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
