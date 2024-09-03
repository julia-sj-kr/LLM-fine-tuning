import speech_recognition as sr
from openai import OpenAI
import serial
import time

# 음성 인식 객체 초기화
rec = sr.Recognizer()

# 아두이노 직렬 포트 설정
arduino_serial = serial.Serial('COM3', 9600, timeout=1)

# OpenAI API 클라이언트 설정
client = OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')

# 음성 명령을 받아들이는 함수
def listen_for_command():
    with sr.Microphone() as source:
        print('"안녕 GPT!"라고 하고 명령을 주세요~')
        while True:
            audio = rec.listen(source)
            try:
                text = rec.recognize_google(audio, language='ko-KR')
                print(text)
                if '안녕 GPT' in text:
                    print('준비됐습니다. 무엇을 할까요?')
                    while True:
                        audio = rec.listen(source)
                        try:
                            command_text = rec.recognize_google(audio, language='ko-KR')
                            print(command_text)
                            return command_text
                        except sr.UnknownValueError:
                            print('다시 명령을 말씀해 주세요~')
            except sr.UnknownValueError:
                print('잘 못들었습니다. 저를 부르셨나요?')

# GPT 모델을 사용해 명령어를 방향으로 변환하는 함수
def get_direction_from_gpt(command_text):
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': '명령어가 주어지면, 그것을 위, 아래, 왼쪽, 오른쪽 중 하나로 변환하십시오.'},
            {'role': 'user', 'content': command_text}
        ]
    )
    direction = response.choices[0].message.content.strip()
    return direction

# 아두이노에 명령을 보내는 함수
def send_to_arduino(command):
    print(f"Sending command to Arduino: {command}")
    arduino_serial.write(command.encode())
    time.sleep(0.1)
    line = []
    for c in arduino_serial.read():
        line.append(chr(c))
    print('Echo :', ''.join(line))

# 메인 함수
def main():
    while True:
        command = listen_for_command()
        if command:
            direction = get_direction_from_gpt(command)
            if direction in ['U', 'D', 'L', 'R']:
                send_to_arduino(direction)
                print(f"Sent command '{direction}' to Arduino.")
            else:
                print("알 수 없는 명령입니다. 다시 시도해 주세요.")

if __name__ == '__main__':
    main()
