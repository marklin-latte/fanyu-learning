# 題目:
# 將 person 中的 age 欄位值讀取出來並且
# 1. 發現年紀謊報所以給他乘 2
# 2. 但發現他有點帥，所以給他一個 description 欄位

# 結果輸出:
# 預設執行指令 python T1/task2.js 輸出結果為:
# {'name': 'mark', 'age': 36, 'description': '馬克好像有點帥'} 

# 目標:
# - 學習什麼是 class/object
# - 學習如何改變 object 屬性 

# 馬克的小提醒
# - 我沒有那麼老

# 參考資料:
# https://www.w3schools.com/python/python_classes.asp
# https://stackoverflow.com/questions/4443301/python-adding-fields-to-objects-dynamically



# ================ 寫程式碼的地方 ==================
# tip: 讀取 person 的 age 欄位，然後放到 input 中

person = {
    'name': 'mark',
    'age': 18
}


# ==================================
# 將結果輸出
print(person['age'])
