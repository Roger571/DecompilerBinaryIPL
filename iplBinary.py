# Decompiler binary IPl files by Roger571 04/02/18
import struct

instForm = "%d, dummy, %d, %f, %f, %f, %f, %f, %f, %f, %d"
carsForm = "%f, %f, %f, %f, %d, %d, %d, %d, %d, %d, %d, %d"

header_fmt = '=4s18i'
header_len = struct.calcsize(header_fmt)
header_unpack = struct.Struct(header_fmt).unpack_from

inst_fmt = "=7f3i"
inst_len = struct.calcsize(inst_fmt)
inst_unpack = struct.Struct(inst_fmt).unpack_from

cars_fmt = "=4f8i"
cars_len = struct.calcsize(cars_fmt)
cars_unpack = struct.Struct(cars_fmt).unpack_from

class iplBinary():
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "rb")
        self.data = f.read()
        s = header_unpack(self.data)
        self.header = s
        if self.header[0] == "bnry": print "[%s] Its IPL!" % self.filename
        else: 
            print "[%s] Unknown type file!" % self.filename
            return 0
           
    def Process(self):
        print "[%s] Count INST: %d [%d]" % (self.filename, self.header[1], self.header[7])
        print "[%s] Count CARS: %d [%d]" % (self.filename, self.header[5], self.header[15])
        
        self.inst = self.readIPL(self.header[1], self.header[7])
        self.cars = self.readIPL(self.header[5], self.header[15], 1)
        
    def readIPL(self, count, offset, type = 0):
        retData = []
        if type == 0:  
            for i in range(0, count):
                print "[%s][readINST] %d | Offset: %d" % (self.filename, i + 1, offset + inst_len * i) 
                retData.append(inst_unpack(self.data, offset + inst_len * i))
        else:
            for i in range(0, count):
                print "[%s][readCARS] %d | Offset: %d" % (self.filename, i + 1, offset + inst_len * i) 
                retData.append(cars_unpack(self.data, offset + cars_len * i))
        return retData
        
    def writeDecompile(self, filename):
        f = open(filename, "w")
        f.write("# Decompiler binary IPL files by Roger571 04/02/18\n")
        f.write("inst\n")
        for i in self.inst:
            f.write(instForm % (i[7], i[8], i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[9]))
            f.write("\n")
        f.write("end\n")
        
        f.write("cars\n")
        for i in self.cars:
            f.write(carsForm % i)
            f.write("\n")
        f.write("end\n")
        f.close()