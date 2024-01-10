pip install openai
import openai

openai.api_key = "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" # Update the API key accordingly.

def get_gpt_response(prompt, max_tokens = 200):
  prompt = f" Answer the following question: {prompt}\nAnswer: "
  response = openai.Completion.create(
      engine = "gpt-3.5-turbo-0301", # Add the current and suitable GPT model.
      prompt = prompt,
      max_tokens = 500,
      n=1,
      temperature = 0.7
  )
  return response.choices[0].text.strip()

prompt = "How add 2 numbers in Python?"
response = get_gpt_response(prompt)
print(response)
