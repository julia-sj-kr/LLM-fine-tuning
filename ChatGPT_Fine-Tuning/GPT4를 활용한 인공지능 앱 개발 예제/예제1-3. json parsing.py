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
                   except sr.UnknownValueError:
                      print('잘 못들었습니다. 다시 명령해주세요~')                   
        except sr.UnknownValueError:
            print('잘 못들었습니다. 다시 말씀해 주세요~')

from openai import OpenAI
client = OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')

#여기에 챗지피티에 물어본 json 코드를 넣어준다.
#def get_machine_script(command):
#return 'json command'

def get_machine_script(command):
    system_message=read_system_prompt()
    response=client.chat.completions.create(
    model='gpt-4o',
    messages=[
            system_message,
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content

def read_system_prompt():
    content=''
    with open('예제1-3. file1.txt','r',encoding="UTF-8") as file:
        content+=file.read()+'\n'*2
    with open('예제1-3. file2.txt','r',encoding="UTF-8") as file:
        content+=file.read()
    return{"role": "user", "content": content}

import json

def execute_machine_script(script):
    actions=json.loads(script)['Machina_Actions']
    for action_key, action in actions.items():
        #print(action_key, action)
        if 'movements' in action and action['movements']:
            execute_movements(action['movements'])
            
motor_mapping={
    'motor_neck_vertical': 3,
    'motor_neck_horizontal': 5,
    #이와 같은 방식으로 모터와 핀을 추가할 수 있다.
    }

import time

def execute_movements(movements):
#    print(movements)
    for movement_key, movement in movements.items():
        print(movement_key, movement)
         
        angle_v=movement.get('motor_neck_vertical',None)
        angle_h=movement.get('motor_neck_horizontal',None)
        speed=movement.get('speed','medium')
        print(angle_v,angle_h,speed)
        
        pin_v=motor_mapping.get('motor_neck_vertical',None)
        pin_h=motor_mapping.get('motor_neck_horizontal',None)
        print(pin_v,pin_h)
        if angle_v:
            command=f'{pin_v},{angle_v},{speed}'
            send_to_arduino(command)
            print(command)
            time.sleep(1)
        if angle_h:
            command=f'{pin_h},{angle_h},{speed}'
            send_to_arduino(command)
            print(command)
            time.sleep(1)

import serial
arduino_serial=serial.Serial('COM1',9600,timeout=1)

def send_to_arduino(command):
    print(command)
    arduino_serial.write(command.encode())#문자열을 2진수로 바꿔서 보내준다.
    line=[]
    time.sleep(0.1)
    
    for c in arduino_serial.read():
        #line.append(chr(c))
        print('Echo : ',chr(c),end='')    
        #print('Echo : ', line)
        
def main():
    while True:
        command=listen_for_command() # 위를 봐
        if command:
          script=get_machine_script(command) # 위를 봐 -> GPT ->JSON
          #print(script)
          #script는 json 파일
          execute_machine_script(script) # JSON -> parsing -> dict
          #실행하기
                  
if __name__=='__main__':
    main()
