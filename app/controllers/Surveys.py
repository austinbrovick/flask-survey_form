from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        print "********* Made it to index method on surveys"
        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        print "************* Made it to process ************"
        return redirect('/result')

    def result(self):
        print "**************** Made it to result method **********"
        return self.load_view('success.html')
