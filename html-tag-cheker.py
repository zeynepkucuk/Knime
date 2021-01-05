class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
def htmltagchecker(filename):
    datas = open(filename)
    s = Stack()
    balanced = True
    search = datas.read()
    searchlist = search.split()
    for i in searchlist:
      if i[0] == "<" and i[1] != "/":
            s.push(i) 
      elif i[0] == "<" and i[1] == "/":
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,i):
                    balanced = False
      else:
            pass
    if balanced and s.isEmpty():
        return True
    else:
        return False
    datas.close()
def matches(open,close):
    opens = ["<html>", "<br>","<body>", "<a>","<base>", "<big>", "<center>", "<code>","<input>","<q>","<select>"]
    closes = ["</html>","</br>","</body>","</a>","</base>","</big>","</center>","</code>","</input>", "</q>","</select>"]
    return opens.index(open) == closes.index(close)
print (htmltagchecker("dosya1.txt"))
print (htmltagchecker("dosya2.txt"))