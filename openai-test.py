import os, dotenv
from openai import OpenAI

dotenv.load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":"You are a talented blog writer who takes on the persona of the Web Wizard to guide readers through technical content."},
        {"role": "user", "content": "Write a short twitter post about AWS EC2 instance storage options."}
    ]
)

print(completion.choices[0].message)
