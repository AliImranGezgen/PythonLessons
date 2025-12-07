def taskAdded(thingsToDo) :
    global toDoList
    toDoList = list(map(str, thingsToDo.split(", ")))
    printToDoList(toDoList)
def taskDelete(deleteTaskIndex) :
    global toDoList
    toDoList.pop(deleteTaskIndex-1)
    printToDoList(toDoList)
def markAsDone(marsAsDoneIndex) :
    global toDoList
    toDoList[index-1] = "[+]" + toDoList[index-1]
    printToDoList(toDoList)
def printToDoList(toDoList):
    a = 1;
    for i in toDoList :
        print(f"{a} - {i}")
        a = a+1



toDoList = []
control = " "; continueCont = "Evet"
while continueCont == "Evet" or continueCont == "evet":
    control = input("Yapmak istediginiz islemi seciniz :\n  -Gorev eklemek icin 'ekle' yaz.\n  -Gorev silmek icin 'sil' yaz.\n  -Gorevi tamamlandi olarak isaretlemek icin 'isaret' yaz.\nKomut giriniz : ")
    if control == "ekle" :
        thingsToDo = input("Yapilacaklar listenize eklenecek gorevleri virgulle (,) ayirarak yaziniz : ") 
        taskAdded(thingsToDo)
    elif control == "sil" :
        printToDoList(toDoList)
        index = 0
        index = int(input("Silmek istediginiz gorevin numarasini giriniz :"))
        if index >0 and index <= (len(toDoList)+1):
            taskDelete(index)
        else: 
            print("Lutfen gecerli bir sayi giriniz :")
    elif control == "isaret":
        printToDoList(toDoList)
        index = 0
        index = int(input("İsaretlemek istediginiz gorevin numarasini giriniz :"))
        if index > 0 and index <= (len(toDoList)+1):
            markAsDone(index)
        else: 
            print("Lutfen gecerli bir sayi giriniz :")
    else :
        control = input("Lutfen ekle, sil veya isaret komutlarindan birini seciniz. : ")
    continueCont = input("Listenizde islem yapmaya devam etmek istiyorsaniz 'evet/Evet', istemiyorsaniz 'hayir/Hayir' giriniz.e\nKomut giriniz : ")