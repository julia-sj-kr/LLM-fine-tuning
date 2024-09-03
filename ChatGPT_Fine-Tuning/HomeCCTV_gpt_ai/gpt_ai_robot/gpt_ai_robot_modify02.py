import speech_recognition as sr

rec=sr.Recognizer()

def listen_for_command():
	with sr.Microphone() as source:
		print('"안녕"라고 하고 명령을 주세요~')
		while True:
			audio=rec.listen(source)        
			try:
				text=rec.recognize_google(audio,language='ko-KR')
				print(text)
				if '안녕' in text:
					print('준비됐습니다. 무엇을 할까요?') # text to speech 추가 가능
					while True:
						audio=rec.listen(source) # 불 켜
						try:
							command_text=rec.recognize_google(
								audio,language='ko-KR')
							print(command_text)
							return command_text
						except sr.UnknownValueError:
							print('다시 명령을 말씀해 주세요~')
			except sr.UnknownValueError:
				print('잘 못들었습니다. 저를 부르셨나요?')    

from openai import OpenAI
#import pyttsx3 # 추가1

client=OpenAI(api_key='Open AI 유료 Key를 입력해주세요.')
#engine = pyttsx3.init() # 추가2

def get_machine_script(command):
	system_message=read_system_prompt()
	response=client.chat.completions.create(
		model='gpt-4o',
		messages=[
			system_message,
			{'role':'user','content': command}
		]
	)
	return response.choices[0].message.content

def read_system_prompt():
	content=''
	with open('file1.txt','r', encoding="UTF-8") as file:
		content+=file.read()+'\n'*2
	with open('file2.txt','r', encoding="UTF-8") as file:
		content+=file.read()
	return {'role':'system','content':content}

import json # 추가하기

def execute_machine_script(script):
	actions=json.loads(script)['Machina_Actions']
	for action_key, action in actions.items(): # 수정
		#print(action_key, action)
		if 'movements' in action and action['movements']: # 추가
			execute_movements(action['movements']) # 추가
motor_mapping={
	'motor_neck_vertical':19,
	'motor_neck_horizontal':18,
	# 이와 같은 방식으로 모터와 핀을 추가할 수 있다.
}
import time
def execute_movements(movements):
	print(movements)
	for movement_key, movement in movements.items():
		print(movement_key, movement)
		angle_v=movement.get('motor_neck_vertical',None)
		angle_h=movement.get('motor_neck_horizontal',None)
		speed=movement.get('speed','medium')
		print(angle_v, angle_h, speed)
		
		pin_v=motor_mapping.get('motor_neck_vertical',None)
		pin_h=motor_mapping.get('motor_neck_horizontal',None)
		print(pin_v, pin_h)
		if angle_v:
			command=f'{pin_v},{angle_v},{speed}'
			if angle_v==90: command='F'
			elif angle_v<90: command='U'
			elif angle_v>90: command='D'
			send_to_arduino(command)
			print(command)
			time.sleep(1)
		if angle_h:
			command=f'{pin_h},{angle_h},{speed}'
			if angle_h==90: command='F'
			elif angle_h<90: command='L'
			elif angle_h>90: command='R'
			print(command)
			send_to_arduino(command)
			time.sleep(1)

import serial
arduino_serial=serial.Serial('COM3', 9600, timeout=1)
def send_to_arduino(command):
	print(command)
	arduino_serial.write(command.encode())
	time.sleep(0.1)
#	line=[]
#	for c in arduino_serial.read():
#	line.append(chr(c))
#	print('Echo :', line)

def main():
	while True:
		command=listen_for_command()
		if command:
			script=get_machine_script(command)
			#print(script)
			#engine.say(script) # 추가3
			#engine.runAndWait() # 추가4
			execute_machine_script(script)
			

if __name__=='__main__':
	main()

