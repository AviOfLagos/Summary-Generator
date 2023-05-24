from flask import Flask, render_template, request, session
import openai

app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
@app.route('/index.html')
def index():
     # Increment the summary count
    session['summary_count'] = session.get('summary_count', 0) + 1

    # Increment the user count
    session['user_count'] = session.get('user_count', 0) + 1

    # Render the template and pass the data as context variables
    return render_template('index.html', summary_count=session['summary_count'], user_count=session['user_count'])

@app.route('/index_.html')
def index_():
     # Increment the summary count
    session['summary_count'] = session.get('summary_count', 0) + 1

    # Increment the user count
    session['user_count'] = session.get('user_count', 0) + 1

    # Render the template and pass the data as context variables
    return render_template('index_.html', summary_count=session['summary_count'], user_count=session['user_count'])


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

@app.route('/sample-summary')
def sample_summary():
    # Retrieve a custom sample summary from a database or other data source
    sample_summary = "This is a custom sample summary."
 # Retrieve comments from a database or other data source
    comments = ['Comment 1', 'Comment 2', 'Comment 3']  # Example comments

    return render_template('summary.html', summary=sample_summary, comments=comments)

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        # Process and store the user's comment, name, and email
        comment = request.form['comment']
        name = request.form['name']
        email = request.form['email']
        # ...

        # Redirect to a thank you page or display a success message

    # Retrieve comments from a database or other data source
    comments = ['Comment 1', 'Comment 2', 'Comment 3']  # Example comments

    return render_template('comments.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
