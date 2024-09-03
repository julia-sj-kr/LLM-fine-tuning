from openai import OpenAI
client = OpenAI(api_key = "Open AI 유료 Key를 입력해주세요.")

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "너는 C++언어 전문가야. 그리고 니가 가르칠 대상은 C++초보자에 식품영양학 전공자야"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "C++의 참조자가 뭐에요?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "참조자는 말이야"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)