# 題目:
# 將 person 中的 age 欄位值讀取出來

# 結果輸出:
# 預設執行指令 python T1/task1.js 輸出結果為:
# 18

# 目標:
# - 學習什麼是 object
# - 如何讀取 object 的欄位(或叫屬性)
# - 這次作業兩個都練習一下

# 馬克的小提醒:
# 在 python 中看起來有兩種方式都可以表達當物件，雖然有些不同，但非工程師的人員只要選方便就好
# - class/object ( class => 食譜, object => 用這個食譜煮出的菜 )
# - dictionaries

# 參考資料:
# https://www.w3schools.com/python/python_classes.asp
# https://www.w3schools.com/python/python_dictionaries.asp


# ================ 寫程式碼的地方 ==================
# 兩種方法都要 print 喔 !
# 方法 1: class/object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print()

# 方法 2: dictionaries
person = {
    'name': 'mark',
    'age': 18
}
print()


# ==================================
