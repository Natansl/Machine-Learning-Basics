from tkinter.filedialog import askopenfilename
from tkinter import Tk
import pandas as pd

class DataImporter(object):

    def __init__(self, flag):
        self.flag = flag
        self.data = []
        self.label = []

    def __importData__(self):
        Tk().withdraw()
        filename = askopenfilename()
        dataFrame = pd.read_csv(filename)
        return dataFrame

    def setup(self):
        data = self.__importData__()
        data = data.values.tolist()

        if self.flag == "R":
            self.data = data
        elif self.flag == "C":
            for i in range(len(data)):
                for j in range(len(data[0]) - 1):
                    dataLine = data[i][j]
                    self.data.append(dataLine)
                self.label.append(int(data[i][len(data[0])-1]))


