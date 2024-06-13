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
            if someletter <=5:
                Thread(target=bro.codes(self)).start()
                someletter += 1
            else:
                Thread(target=bro.codes(self)).start()
                someletter += 1

class breakitmore():
    def brobreakit(yourword):
        for letters in (yourword):
            bigword = ""
            count = 0
            while count <= len(yourword):
                bigword += letters
                count += 1
            if count >= len(yourword):
                Thread(target=main.brocode(bigword)).start()
        


breakitmore.brobreakit(input())

