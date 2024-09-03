'''
from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="옛날 옛적에\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
'''
from openai import OpenAI
client = OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="옛날 옛적에\n",
  temperature=1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)