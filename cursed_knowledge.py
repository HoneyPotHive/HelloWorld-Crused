from threading import Thread

class bro():
    def codes(self):
        someletter = 1
        while someletter <= 10:
            print(self)
            someletter +=1
    
class main():
    def brocode(self):
        someletter = 1
        while someletter <=10:
            Thread(target=bro.codes(self)).start()
            someletter += 1
            
main.brocode(input())
