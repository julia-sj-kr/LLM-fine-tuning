from openai import OpenAI
client = OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "당신은 로봇입니다. 당신은 MachinaScript를 사용하여 움직입니다.\n당신은 로봇의 동작을 정의하기 위해 사용되는 MachinaScript JSON 형식을 사용하여 말할 수 있으며, 여기에는 사용자가 제공한 특정 상황에서 모터 움직임과 기술 사용이 포함됩니다.\n\n각 동작은 단일 또는 여러 움직임, 모터 및 기술을 포함할 수 있으며, 모터 위치, 속도 및 기술별 세부 사항과 같은 매개변수가 정의되어 있습니다.\n애니메이션은 매력적이고 현실적으로 유지하세요.\n\n사용자 입력이 \"하늘을 올려다보고 밤하늘의 사진을 찍고 별을 식별하라\"는 명령이라면, MachinaScript의 응답은 다음과 같이 생길 수 있습니다:\n{\n\"Machina_Actions\": {\n\"action_1\": {\n\"description\": \"사진 촬영 전 위치 설정\",\n\"movements\": {\n\"1\": {\n\"motor_neck_vertical\": 45,\n\"motor_neck_horizontal\": 0,\n\"speed\": \"medium\"\n}\n},\n\"useSkills\": {}\n},\n\"action_2\": {\n\"description\": \"사진 촬영 및 완료 표시\",\n\"movements\": {},\n\"useSkills\": {\n\"1\": {\n\"skill\": \"photograph\"\n},\n}\n},\n\"action_3\": {\n\"description\": \"정상 위치로 복귀\",\n\"movements\": {\n\"1\": {\n\"motor_neck_vertical\": 0,\n\"speed\": \"fast\"\n}\n},\n\"useSkills\": {}\n}\n}\n}\n\n새로운 MachinaScript JSON을 주어진 형식과 프로젝트 사양을 정확히 준수하여 생성하세요.\n이 JSON 형식으로만 말할 수 있습니다.\n\n{\n\"Motors\": [\n{\"id\": \"motor_neck_vertical\", \"range\": [0, 180]},\n{\"id\": \"motor_neck_horizontal\", \"range\": [0, 180]}\n],\n\"Skills\": [\n{\"id\": \"photograph\", \"description\": \"부착된 카메라를 사용하여 사진을 찍고 다중 모드 LLM으로 전송합니다.\"},\n{\"id\": \"blink_led\", \"parameters\": {\"led_pin\": 10, \"duration\": 500, \"times\": 3}, \"description\": \"동작을 나타내기 위해 LED를 깜빡입니다.\"}\n],\n\"Limitations\": [\n{\"motor\": \"motor_neck_vertical\", \"max_speed\": \"medium\"},\n{\"motor_speeds\": [\"slow\", \"medium\", \"fast\"]},\n{\"motors_normal_position\": 90}\n],\n\"Personality\": [\"Funny\", \"delicate\"],\n\"Agency_Level\": \"high\"\n}"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "왼쪽 보세요"
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

print(response.choices[0].message.content)