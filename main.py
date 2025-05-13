import pandas as pd
df=pd.read_excel('buildingbuildingtime.xlsx',engine='openpyxl')
# print(df)
# print(df)
def translate(x): #강의실 이름을 입력받으면, 해당 건물과 층수 tuple형태로 반환환
    for building,lst in dict.items():
        for sublst in lst:
           if x in sublst:
               return (building,lst.index(sublst)+1)
           else:
                continue

dict={'정문':[['정문']],
      '창의인재관':[['컴퓨터1실','준비실','정보과학강의실','서버실','정보과학연구실','컴퓨터2실'],['화학R&E실','화학강의실2','화학강의실1','화학연구실1','동아리실','화학 첨단기기실'],['화학실험실1','화학연구실2','화학실험실2','준비실','시약실','화학강의실3'],['강당']],
      '융합인재관':[[]],
      '예지관':[[]],
      '의행관':[['택배함'],['의행관교무실','식당','여자기숙사'],['3학년기숙사'],['2학년기숙사'],['1학년기숙사']],
      '우암관':[[]],
      '아람관':[['아람관']]}
buildinglist=list(dict.keys())
#key는 건물명, 이후 중첩 리스트에는 각 층별로 있는 강의실 이름
#번호 예시:수학강의실2 를 붙일지 고민
print(translate(input()))