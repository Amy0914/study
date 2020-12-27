class SequenceList:
    #（1）创建一个顺序表。（2）对该顺序表进行初始化。
    def __init__(self):
        self.SeqList = []

    #创建顺序表,append()方法在顺序表尾端直接插入新元素
    def CreateSequenceList(self):
        Element = input("请输入元素：")
        while Element != '#':
            self.SeqList.append(int(Element))
            Element = input("请输入元素：")

    #查找顺序表中某一元素
    def FindElement(self,SeqList):
        key = int(input("请输入要查找的元素："))
        if key in self.SeqList:
            ipos = self.SeqList.index(key)
            print("查找成功，值为：",self.SeqList[ipos],"位置为：",ipos+1)
        else:
            print("查找失败")

    #指定位置插入元素
    def InsertElement(self, SeqList):
        ipos = int(input("输入元素位置："))
        Element = int(input("输入元素："))
        self.SeqList.insert(ipos,Element)
        print("插入元素后，当前表为：",self.SeqList)

     #删除指定位置元素
    def DeleteElement(self,SeqList):
        ipos = int(input("删除元素的位置："))
        self.SeqList.remove(self.SeqList[ipos])
        print("删除元素后，当前表为：",self.SeqList)

    #遍历顺序表元素
    def TraverseElement(self):
        Len = len(self.SeqList)
        for i in range(0,Len):
            print("元素值分别为：",self.SeqList[i])

if __name__ == '__main__':
    list = SequenceList()
    list.CreateSequenceList()
    list.FindElement(list)
    list.InsertElement(list)
    list.DeleteElement(list)
    list.TraverseElement()