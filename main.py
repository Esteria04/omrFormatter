import json
def formatter():
	filename = input("문제집 아이디 입력:: ")
	result = {}
	chapter = input("단원명을 입력해 주세요 (','를 이용해 분할해 주세요):: ").upper()
	chapters = chapter.split(',')
	for c in chapters:
		qList = []
		while True:
			ans = input(f"단원{c} 작성중:: ").upper()
			if ans == "!":
				break
			qList.append(ans)
		result[f"{c}"] = qList
	with open(f"./{filename}.json", 'w', encoding='utf-8') as file:
		json.dump(result, file, indent="\t")
formatter()
