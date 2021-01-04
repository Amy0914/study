class liststudy:
    def __init__(self):
        self.SeqList = []

    def CreateSequenceList(self):
        Element = input("请输入分数：")
        while Element != '#':
            self.SeqList.append(int(Element))
            Element = input("请输入分数：")

    def GetExtremum(self):
        Max = max(self.SeqList)
        print("最高分：", Max)
        Min = min(self.SeqList)
        print("最低分：",Min)

if __name__ == '__main__':
    list = liststudy()
    list.CreateSequenceList()
    list.GetExtremum()