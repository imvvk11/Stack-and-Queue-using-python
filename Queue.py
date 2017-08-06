#OOP implementation of a queue

class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def delete(self):
        itemToDelete = self.items[0]
        del self.items[0]
        return itemToDelete

    def size(self):
        return len(self.items)
    def report(self):
        return self.items

def testQueue():
    myQueue = Queue()
    #myQueue.add("Vivek")
    #myQueue.add("Qazi")
    #myQueue.add("Ahmed")
    #myQueue.add("Hussain")
    #myQueue.add("Hameed")
    #print(myQueue.size())
    #print(myQueue.report())
    #print(myQueue.delete())
    #print(myQueue.report())
                
#testQueue()
