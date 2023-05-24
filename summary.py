from flask import Flask, request
import openai

app = Flask(__name__)

@app.route("/summary")
def summary():
  name = request.form["name"]
  title = request.form["title"]
  summary = request.form["summary"]

  # Generate summary using OpenAI's GPT-4
  response = openai.create_response(
    prompt="Generate a summary of the following: \n\nName: {}\nTitle: {}\nSummary: {}".format(name, title, summary),
    temperature=0.7,
    max_tokens=100,
    top_p=0.9,
    engine="davinci-002"
  )

  # Return the summary to the user
  return response["choices"][0]["text"]

if __name__ == "__main__":
  app.run(debug=True)
