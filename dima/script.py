import json
from utills.ai_rate_1 import rated_1
from utills.ai_rate_2 import rated_2
from utills.ai_rate_3 import rated_3
from utills.ai_rate_4 import rated_4
import time
try:
    sortArr=[]
    rated_value=0
    with open('data.json', 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    
    with open('rated.json', 'r', encoding='utf-8') as file:
        rate = json.load(file)
        
    for i in data:
        try:
            rated_value+=int(rated_1(i,tags))
            time.sleep(2)
        except:
            rated_value+=0
        rated_value-=int(rated_2(i))
        time.sleep(2)
        try:
            rated_value+=int(rated_3(i))
            time.sleep(2)
        except:
            rated_value=0
        try:
            rated_value+=int(rated_4(i))
            time.sleep(2)
        except:
            rated_value=0
        sortArr.append({
                        "id":i["id"],
                        "rate":rated_value,
                        "title":i["title"],
                        "date":i["date"],
                        "link":i["link"],
                        "text":i["text"]
                        })
        rated_value=0
 
    sorted_dicts = sorted(sortArr, key=lambda x: x['rate'])

    rete = json.loads(json.dumps(sorted_dicts))
 

    with open('rated.json', 'w', encoding='utf-8') as file:
        json.dump(rete, file, ensure_ascii=False, indent=4)

except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования JSON: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
