import json
import os

def mkdir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def InputMach():
	def help(): 
		print("""
----------------------------------------------------------------------------------------------
주관식은 0숫자 ex) 24 => 024, 223 => 0223 형태로 입력하시고, 객관식은 12345 중 하나를 입력해 주세요.

[명령어 목록]
			  
	[//] 단원 단위에서 답안 작성이 완료되었을 경우 다음 단원으로 넘어갈 때 입력해 주세요.
			  
			  ex) A단원 마지막문제:: 342
				  A단원 마지막문제+1:: // (마지막 문제보다 번호가 1 클 때 입력하시면 됩니다)			  	  

	[..] 중간에 뛰어넘거나 잘못 입력했을 경우, '..'을 입력해 주시면 이전 번호로 돌아갑니다.
			  
			  ex) 대충 아무 문제:: 
			      대충 아무 문제2:: ..
			      대충 아무 문제:: 1 (이렇게 명령어를 입력하면 이전 번호로 돌아갑니다)

	[/exit] 중간에 그만둘 때 입력해 주세요. 주의! 작업한 이전 단원은 저장되지만, 작성중이던 단원은 저장되지 않습니다.

	[/help] 이 메시지를 다시 보고 싶으시면 '/help'를 입력해 주세요.
			  
	이용해 주셔서 감사합니다.
""")
	help()
	filename = input("단원 묶음이 저장될 폴더명을 입력해 주세요:: ")
	mkdir(f"./{filename}")
	chapter = input("답안을 작성할 단원명을 입력해 주세요 (','를 이용해 분할해 주세요):: ").upper()
	chapters = chapter.split(',')
	for c in chapters:
		qList = []
		while True:
			ans = input(f"{c}단원 {len(qList)+1}번 문제:: ").upper()
			if ans == "//":
				break
			elif ans == "/help":
				help()
				continue
			elif ans == "..":
				del qList[-1]
				continue
			elif ans == '/exit':
				return
			qList.append(ans)
		with open(f"./{filename}/{c}단원.json", 'w', encoding='utf-8') as file:
			json.dump(qList, file)

def EncodeMach(dir, filename, chapters):
	result = []
	for c in chapters:
		with open(f"./{c}단원.json") as file:
			data = json.load(file)
		counter = 1
		for d in data:
			dictBox = {}
			dictBox["Chapter"] = c
			if d[0] == "0":
				dictBox["Type"] = "D"
				dictBox["Answer"] = d[1:]
			else:
				dictBox["Type"] = "O"
				dictBox["Answer"] = d
			dictBox["Number"] = str(counter)
			result.append(dictBox)
			counter += 1
	with open(f"./{dir}/{filename}.json", 'w', encoding='utf-8') as res:
		json.dump(result, res, indent="\t")
		
def typeFn():
	text = """
	ONLINE MARKING READER ver 1.0.0 을 이용해 주셔서 감사합니다. 
	
	본 프로그램은, 답지를 웹사이트에서 읽을 수 있는 형식으로 변환하는 작업을 수행합니다.

	폴더명은 파일명과 동일하게 입력 부탁드립니다.
	"""
	print(text)
	inp = input("답안을 입력하시려면 0, 단원별 답안을 합치시려면 1을 입력해 주세요:: ")
	if inp=='0':
		InputMach()
	elif inp=='1':
		EncodeMach(input("파일 저장할 폴더명 입력:: "),input("저장할 파일명 입력:: "),list(input("단원 입력:: ").upper()))

typeFn()