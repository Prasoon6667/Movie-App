import sys
import movie_details
import urllib
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

class Layout(QtGui.QWidget):
    
    def __init__(self):
        super(Layout, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        
        self.qle = QtGui.QLineEdit(self) 
        self.qle.move(30, 30)
        self.qle.setText("Enter movie name ")


        self.btn = QtGui.QPushButton("Submit",self)
        self.btn.move(170, 30)
        self.btn.clicked.connect(self.buttonClicked)
        

        self.qle_list = QtGui.QTextEdit(self) 
        self.qle_list.move(30, 80)
        self.qle_list.resize(220,250)


        self.select_movie = QtGui.QLineEdit(self) 
        self.select_movie.move(30, 350)
        self.select_movie.resize(380,25)
        self.select_movie.setText("To know more about a movie, copy and paste movie here & click below button")


        self.get_details_btn = QtGui.QPushButton("Get Details",self)
        self.get_details_btn.move(30, 380)
        self.get_details_btn.clicked.connect(self.get_details_from_list)

        
        self.pic = QtGui.QLabel(self)
        self.img = QtGui.QImage()
        self.pic.move(500, 30)
        pixmap = QtGui.QPixmap("pic.jpg")
        self.pic.setPixmap(pixmap)
        # data = urllib.urlopen("http://ia.media-imdb.com/images/M/MV5BMzJhNjMyOGMtYjhiYy00ZTAwLThmZWUtZmE5NzI3OTk4Y2M4XkEyXkFqcGdeQXVyMzQ5Njc3NzU@._V1_UY268_CR9,0,182,268_AL_.jpg").read()
        # self.img.loadFromData(data)
        # self.pic.setPixmap(QPixmap(self.img).scaledToWidth(200))

        self.dir = QtGui.QLabel(self)
        self.dir.move(700, 30)
        self.dir.setText("Director :")
        self.dir.hide()


        self.dir_btn = QtGui.QLabel(self)
        self.dir_btn.move(750, 30)
        self.dir_btn.resize(380,25)
        self.dir_btn.setText("None")
        self.dir_btn.hide()

        self.writer = QtGui.QLabel(self)
        self.writer.move(700, 80)
        self.writer.setText("Writers :")
        self.writer.hide()

        self.writer_btn = QtGui.QLabel(self)
        self.writer_btn.move(750, 80)
        self.writer_btn.resize(380,15)
        self.writer_btn.setText("None")
        self.writer_btn.hide()

        self.actor = QtGui.QLabel(self)
        self.actor.move(700, 120)
        self.actor.setText("Actors :")
        self.actor.hide()

        self.actor_btn = QtGui.QLabel(self)
        self.actor_btn.move(750, 120)
        self.actor_btn.resize(380,15)
        self.actor_btn.setText("None")
        self.actor_btn.hide()


        self.setGeometry(500, 500, 900, 500)
        self.setWindowTitle('Movie Details')
        self.show()

    def buttonClicked(self):

        movie = self.qle.text()
        obj = movie_details.Scrape()
        url = obj.geturl(movie)
        self.link_dict = obj.connect(url)
        names = 'We have found these much of movies \n'
        
        for key,value in self.link_dict.iteritems():

            names = names + key
            names = names + "\n"
            
            
        print names
        self.qle_list.setText(names)


    def get_details_from_list(self):

        print "Button clicked"
        selected_movie = self.select_movie.text()
        selected_movie = selected_movie + " "
        obj = movie_details.Scrape()
        if selected_movie in self.link_dict.keys():
            link = self.link_dict[str(selected_movie)]
            url = obj.get_search_link(link)
            self.details_dict = obj.connect_search_link(url)

            image_url = self.details_dict['poster']
            data = urllib.urlopen(image_url).read()
            self.img.loadFromData(data)
            self.pic.setPixmap(QPixmap(self.img).scaledToWidth(180))
            
            
            director = self.details_dict['director']
            self.dir_btn.setText(director)
            
            writer = self.details_dict['writer']
            self.writer_btn.setText(writer)

            actors = self.details_dict['actors']
            self.actor_btn.setText(actors)
            self.dir.show()
            self.dir_btn.show()
            self.writer.show()
            self.writer_btn.show()
            self.actor.show()
            self.actor_btn.show()
            # print value
            



        
           
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()