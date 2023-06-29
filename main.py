import customtkinter as ctk
import random

num = [1,2,3,4,5,6,7]
problem = {"40":"สี่สิบ",
               "58":"ห้าสิบแปด",
               "69":"หกสิบเก้า",
               "72":"เจ็ดสิบสอง",
               "705":"เจ็ดร้อยห้า",
               "1025":"หนึ่งพันยี่สิบห้า",
               "540":"ห้าร้อยสี่สิบ"}

question = {1:"40",
           2:"58",
           3:"69",
           4:"72",
           5:"705",
           6:"1025",
           7:"540"}

score = 0
# สร้างฟังก์ชั่นสำหรับสุ่มหาคำถาม
def question():
    problem = {"40":"สี่สิบ",       #สร้าง dict คำตอบ กับ คำถาม เพื่อไว้ใช้แปลงข้อมูลจากคำตอบเป็นคำถาม
               "58":"ห้าสิบแปด",
               "69":"หกสิบเก้า",
               "72":"เจ็ดสิบสอง",
               "705":"เจ็ดร้อยห้า",
               "1025":"หนึ่งพันยี่สิบห้า",
               "540":"ห้าร้อยสี่สิบ"}

    question = {1:"40",   # สร้าง dict ตัวเลขลำดับข้อ กับ คำตอม เพื่อไว้ใช้แปลงข้อมูลจากการสุ่มตัวเลขลำดับ
           2:"58",        # แต่ไม่ต้องสร้างแล้วเปลี่ยนการสุ่ม เป็นการสุ่มคำตอบแทนก็ได้
           3:"69",
           4:"72",
           5:"705",
           6:"1025",
           7:"540"} 
    if len(num) != 0: # นับจำนวนสมาชิกข้อมูลที่อยู่ในตัวแปรชื่อ num 
        random_choice = random.choice(num)    # สุ่มตัวเลขออกมา
        random_ans = question[random_choice]  # เแล้วเอาตัวเลขมาแปลข้อมูลกับ dict question
        random_question = problem[random_ans] # แล้วเอาข้อมูลที่แปลแล้วมาแปลอีกด้วย dict probleam
        question_label.configure(text= str(random_question)) # เปลี่ยนข้อความใน label
        num.remove(random_choice)

# ฟังก์ชั่นสำหรับกดตอบ
def answer():
    global score
    button = ans_button.cget("text") # ดึงข้อความบนปุ่ม
    
    if button == "Start": # ตรวจสอบข้อความบนปุ่ม
        ans_button.configure(text="Answer") # เปลี่ยนข้อความบนปุ่ม
        question() # เรียกใช้ฟังก์ชั่นสุ่มคำถาม
    else:
        label = question_label.cget("text") # ดึงข้อความมาจาก label มาเก็บในตัวแปร
            
        ans = str(ans_entry.get()) # ดึงข้อมูลจาก entry
        """
            ใช้ try except ตรวจสอบข้อมูลในกรณีที่คำตอบไม่มีใน dict
        """
        try:

            if problem[ans] == label:
                score += int(100/len(num))
                print(score)
                score_label.configure(text=score)
                #print(score_label.cget("text"))
                question()
            else:
                score -= int(100/len(num))
                print(score)
                score_label.configure(text=score)
                #print(score_label.cget("text"))
                question()

        except:
            """
                ใช้ try except ตรวจสอบว่าเกมจบหรือยัง ถ้าเกมยังไม่จบจะทำงานในส่วนของ
                try แต่เมื่อเกมจบ หรือ สมาชิกของ list ในตัวแปร num หมดจะเกิด error
                แล้วจะเริ่มทำงานโค้ดในส่วนของ except
            """
            try:
                score -= int(100/len(num))
                print(score)
                score_label.configure(text=score)
                #print(score_label.cget("text"))
                question()
            except:
                score = score_label.cget("text")
                score = "Your Score :" + str(score)
                question_label.configure(text=score)

    
    
app = ctk.CTk()
app.title("Q&A")
app.geometry("400x400")

head_label = ctk.CTkLabel(app, text="Q&A", font=('Nawabiat',40),
                          fg_color="#7DFAB6", text_color="#007074",
                          corner_radius=40, padx=30, pady=30)
head_label.pack()

question_label = ctk.CTkLabel(app, text=" ", font=('Nawabiat',40))
question_label.pack(pady=(20,0))

ans_entry = ctk.CTkEntry(app)
ans_entry.pack()

ans_button = ctk.CTkButton(app, text="Start", command=answer)
ans_button.pack()

score_label = ctk.CTkLabel(app, text= '', font=('Nawabiat',30))
score_label.pack(pady=(150,0))
score_label.pack(padx=(250,0))

app.mainloop()
