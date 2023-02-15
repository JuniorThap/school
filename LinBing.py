import pandas as pd

df = pd.read_excel("Stock.xlsx")
df_edit = df

def ChangeAmt(search):
    inout = input("นำออกหรือนำเข้า:")
    if inout == "นำเข้า":
        inOrout = 1
    elif inout == "นำออก":
        inOrout = -1
    else:
        print("กรุณาลองอีกครั้ง")
        ChangeAmt(search) 
    change_amt = int(input("จำนวน:"))
    print(inout,end="")
    print(f" {search} จำนวน {change_amt} ชิ้น")
    save_inout = (input("ต้องการบันทึกข้อมูลหรือไม่ (ใช่ / ไม่):"))
    amt = int(df.Amount[df.Name==search])
    new_amt = amt+(change_amt*inOrout)
    save = save_inout == "ใช่"
    if save | (save_inout == "ไม่"):
        df_edit.replace(to_replace=amt,value=new_amt,inplace=save)
        print("ทำรายการสำเร็จ")
        Main()
    else:
        print("กรุณาลองอีกครั้ง")
        ChangeAmt(search)

def SearchItem():
    print("เมนูค้นหาสินค้า")
    search = input("ชื่อสินค้า:")
    found = list(df.Name.str.match(search)).__contains__(True)
    if found:
        ChangeAmt(search)
    else:
        print(f"ไม่พบสินค้า {search} กรุณาลองอีกครั้ง")
        SearchItem()

def AddNewItem(df):
    global df_edit
    df = pd.read_excel("Stock.xlsx",index_col="Name")
    print("เมนูเพิ่มสินค้า")
    new_name = input("ชื่อสินค้า:")
    new_category = input("ประเภทสินค้า:")
    new_price = input("ราคาสินค้า:")
    new_amount = input("จำนวนสินค้า:")
    save_add = input("ต้องการบันทึกรายการหรือไม่ (ใช่ / ไม่):")
    new_product = [[new_name,new_category,new_price,new_amount]]
    cols = ["Name","Category","Price","Amount"]
    if save_add == "ใช่":
        new_row = pd.DataFrame(data=new_product,columns=cols)
        df_edit = df_edit.append(new_row,ignore_index=False)
        df_edit = df_edit.reset_index()
        df_edit.drop("index",axis=1,inplace=True)
        print("ทำรายการสำเร็จ")
        Main()
    elif save_add == "ไม่":
        print("ทำรายการสำเร็จ")
        Main()
    else:
        print("กรุณาลองอีกครั้ง")
        AddNewItem(df)

def DelItem(df,df_edit):
    df = pd.read_excel("Stock.xlsx")
    print("เมนูลบสินค้า")
    search_del = input("ชื่อสินค้า:")
    match_del = list(df.Name.str.match(search_del)).__contains__(True)
    if not match_del:
        print("ไม่พบสินค้า กรุณาลองอีกครั้ง")
        DelItem(df,df_edit)
    print("พบสินค้า\t",search_del)
    save_del = input("ต้องการบันทึกการลบหรือไม่ (ใช่ / ไม่):")
    if save_del == "ใช่":
        index = df_edit[df_edit.Name.str.match(search_del)].index
        df_edit.drop(index,axis=0,inplace=True)
        print("ทำรายการเสร็จสิ้น")
        Main()
    elif save_del == "ไม่":
        print("ทำรายการเสร็จสิ้น")
        Main()
    else:
        print("กรุณาลองอีกครั้ง")
        DelItem(df,df_edit)

def EndNSave():
    print("สิ้นสุดการทำงานและบันทึกไฟล์")
    df_edit.set_index("Name")
    df_edit.to_excel("Stock(edited).xlsx")
    print("บันทึกไฟล์สำเร็จ")

def Main():
    choose = int(input("1 = สำหรับเมนูค้นหาสินค้า\n2 = สำหรับเมนูเพิ่มสินค้า\n3 = สำหรับเมนูลบสินค้า\n4 = สำหรับการสิ้นสุดการทำงานและบันทึกไฟล์\n"))
    if choose == 1:
        SearchItem()
    elif choose == 2:
        AddNewItem(df)
    elif choose == 3:
        DelItem(df,df_edit)
    elif choose == 4:
        EndNSave()
    else:
        print("กรุณาลองอีกครั้ง")
        Main()
    print("\n")

print("\nโปรแกรมจัดการร้านค้า")
Main()