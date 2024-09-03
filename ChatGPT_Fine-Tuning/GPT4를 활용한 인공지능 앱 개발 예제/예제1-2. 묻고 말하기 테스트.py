'''
import speech_recognition as sr

rec=sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print('say \'hello robot\'then command.')
        audio=rec.listen(source)
        
        text=rec.recognize_google(audio).lower()
        print(text)
    
def main():
    while True:
        command=listen_for_command()
        
if __name__=='__main__':
    main()
'''
import speech_recognition as sr

rec=sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print('"안녕 지니!"라고 명령을 주세요~')
        audio=rec.listen(source)
        
        try:
            text=rec.recognize_google(audio,language='ko-kr')
            print(text)
            if '안녕 지니' in text:
                print('준비됐습니다. 무엇을 할까요?.') #text to speech로 변경 가능
                while True:
                   audio=rec.listen(source)
                   try:
                      command_text=rec.recognize_google(audio,language='ko-kr')
                      print(command_text)
                      return command_text
                   except sr.UnknownValuerError:
                      print('잘 못들었습니다. 다시 명령해주세요~')                   
        except sr.UnknownValueError:
            print('잘 못들었습니다. 다시 말씀해 주세요~')

from openai import OpenAI
client = OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')

import pyttsx3
engine=pyttsx3.init()#음성초기화

#여기에 챗지피티에 물어본 json 코드를 넣어준다.
#def get_machine_script(command):
#return 'json command'

def get_machine_script(command):
#    system_message=read_system_prompt()
    response=client.chat.completions.create(
    model='gpt-4o',
    messages=[
#            system_message,
            {"role": "user", "content": command}
#        {"role": "user", "content": "hello"}
        ]
    )
    return response.choices[0].message.content
 
def main():
    while True:
        command=listen_for_command()
        if command:
          script=get_machine_script(command)
          print(script)
            #script는 json 파일
          engine.say(script)
          engine.runAndWait()
        
if __name__=='__main__':
    main()