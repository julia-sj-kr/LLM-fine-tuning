from openai import OpenAI
client = OpenAI(api_key='OpenAI 유료 KEY 입력해주세요.')

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "너는 신입 개발자에 취업을 지원하는 취업 전문가야."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "나는 초보 자바 개발자인데 포트폴리오 어떻게 작성할지 4줄 말해줄래?"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

print(response.choices[0].message)