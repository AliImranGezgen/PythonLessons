def taskAdded(thingsToDo, toDoList):
    toDoList[:] = [i.strip() for i in thingsToDo.split(",") if i.strip()]

def taskDelete(deleteTaskIndex, toDoList) :
    toDoList.pop(deleteTaskIndex-1)

def markAsDone(marsAsDoneIndex, toDoList) :
    toDoList[marsAsDoneIndex-1] = "[+]" + toDoList[marsAsDoneIndex-1]
    printToDoList(toDoList)

def printToDoList(toDoList):
    a = 1
    for i in toDoList :
        print(f"{a} - {i}")
        a = a+1



toDoList = []
control = " "; continueCont = "Evet"; index = 0
while continueCont.lower() == "evet":
    control = input("Yapmak istediginiz islemi seciniz :\n  -Gorev eklemek icin 'ekle' yaz.\n  -Gorev silmek icin 'sil' yaz.\n  -Gorevi tamamlandi olarak isaretlemek icin 'isaret' yaz.\nKomut giriniz : ")
    if control == "ekle" :
        thingsToDo = input("Yapilacaklar listenize eklenecek gorevleri virgulle (,) ayirarak yaziniz : ") 
        taskAdded(thingsToDo, toDoList)
        printToDoList(toDoList)
    elif control == "sil" :
        printToDoList(toDoList)
        index = int(input("Silmek istediginiz gorevin numarasini giriniz :"))
        if index >0 and index <= (len(toDoList)):
            taskDelete(index, toDoList)
        else: 
            print("Lutfen gecerli bir sayi giriniz :")
    elif control == "isaret":
        printToDoList(toDoList)
        index = int(input("İsaretlemek istediginiz gorevin numarasini giriniz :"))
        if index > 0 and index <= (len(toDoList)):
            markAsDone(index, toDoList)
        else: 
            print("Lutfen gecerli bir sayi giriniz :")
    else :
        control = input("Lutfen ekle, sil veya isaret komutlarindan birini seciniz. : ")
    continueCont = input("Listenizde islem yapmaya devam etmek istiyorsaniz 'evet', istemiyorsaniz 'hayir' giriniz.e\nKomut giriniz : ")