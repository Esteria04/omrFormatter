import json
def formatter():
	def help(): 
		print("""
		  Online Marking Reader 에서 사용되는 문제집 답지를 제작하는 프로그램 입니다.
		  ----------------------------------------------------------------------------------------------
		  먼저 답지가 저장될 파일명을 입력하여 설정해 주시고, 단원을 ',' 를 이용해 나열해서 입력해 주세요.
		  
		  주관식은 d숫자 형태로 입력하시고, 객관식은 그냥 숫자를 입력해 주세요.

		  단원 단위에서 답안 입력이 완료되었을 경우 '//'를 입력하시면 다음 단원의 답안 입력으로 넘어갈 수 있습니다.

		  중간에 잘못 입력하여 처음으로 돌아가려면 '!!'를 입력해 주세요.

		  이 메세지를 다시 보고 싶으시면 '??'를 입력해 주세요.
			  
		  이용해 주셔서 감사합니다.
		  """)
	help()
	filename = input("문제집 아이디 입력:: ")
	result = {}
	chapter = input("단원명을 입력해 주세요 (','를 이용해 분할해 주세요):: ").upper()
	chapters = chapter.split(',')
	for c in chapters:
		qList = []
		while True:
			ans = input(f"{c}단원 {len(qList)+1}번 문제:: ").upper()
			if ans == "//":
				break
			elif ans == "??":
				help()
				continue
			elif ans == "!!":
				return
			qList.append(ans)
		result[f"{c}"] = qList
	with open(f"./{filename}.json", 'w', encoding='utf-8') as file:
		json.dump(result, file, indent="\t")
formatter()
