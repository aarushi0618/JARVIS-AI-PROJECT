from openai import OpenAI
client = OpenAI(
  api_key="YOUR_OPENAI_API_KEY_HERE"
)

# Create the request (Python syntax)
response = client.chat.completions.create(
  model="gpt-3.5-turbo", # Note: gpt-5-nano does not exist yet
  messages=
    {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
  
)
print(response.choices[0].message.content)