import random
import numpy as np
menu = {'ข้าวแกง':25,'ข้าวผัด':30,'โจ๊กหมู':45}
menuName = list(menu.keys())
menuPrice = list(menu.values())
day = ['จันทร์','อังคาร','พุธ','พฤหัส','ศุกร์']
circulationDishTable_Array = np.array([[0]*len(day)]*len(menuPrice))
for i in range(len(menu)):
    for j in range(len(day)):
        circulationDishTable_Array[i,j] = random.randrange(45,121,5)
allDishInOneDay = np.sum(circulationDishTable_Array,axis=0)
eachFoodsDishInOneWeek = np.sum(circulationDishTable_Array,axis=1)
print('\n\tร้านขายอาหารตามสั่งมีราคาอาหารคือ'.expandtabs(6))
print(f'{menuName[0]} {menuPrice[0]} บาท',end='')
for i in range(1,len(menu)-1):
    print(f'/ {menuName[i]} {menuPrice[i]} บาท',end='')
print(f'/ {menuName[len(menu)-1]} {menuPrice[len(menu)-1]} บาท')
print('\tในสัปดาห์ที่ผ่านมาขายอาหารได้ดังนี้')
print('\n\t'.expandtabs(6),end='')
for i in range(len(day)-1):
    print(f'\t{day[i]}'.expandtabs(2),end='')
print(f'\t{day[len(day)-1]}'.expandtabs(2))
for i in range(len(menuName)):
    print(menuName[i],end='')
    for j in range(len(day)-1):
        print('\t'.expandtabs(2),circulationDishTable_Array[i,j],end='')
    print('\t'.expandtabs(2),circulationDishTable_Array[i,len(day)-1])
print('\n\tจำนวนจานทั้งหมดที่ขายได้แต่ละวัน'.expandtabs(1))
for i in range(len(day)-1):
    print(day[i],end='\t'.expandtabs(2))
print(day[len(day)-1])
for i in range(len(allDishInOneDay)-1):
    print(allDishInOneDay[i],end='\t'.expandtabs(3))
print(allDishInOneDay[len(allDishInOneDay)-1])
print('\n\tอาหารแต่ละประเภทที่ขายได้ใน 1 สัปดาห์'.expandtabs(1))
for i in range(len(menuName)-1):
    print(menuName[i],end='\t'.expandtabs(2))
print(menuName[len(menuName)-1])
for i in range(len(eachFoodsDishInOneWeek)-1):
    print(eachFoodsDishInOneWeek[i],end='\t'.expandtabs(5))
print(eachFoodsDishInOneWeek[len(eachFoodsDishInOneWeek)-1])
print('\n\tอาหารที่ขายดีที่สุดใน 1 สัปดาห์'.expandtabs(1))
min = 0
index = 0
for i in range(len(eachFoodsDishInOneWeek)):
    if eachFoodsDishInOneWeek[i] > min:
        min = eachFoodsDishInOneWeek[i]
        index = i
print(menuName[index],'\n')