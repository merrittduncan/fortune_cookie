
import webapp2
import random

def getRandomFortune():
    fortunes = [
    'You will live the longest of all!',
    'Be wary of crustaceans!',
    'Many orchard fruits will come your way!'
    ]
    index = random.randint(0,((len(fortunes))-1))

    return fortunes[index]



class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'
        fortune = getRandomFortune()
        fortune_sentence = "Your fortune: " + str(fortune)
        fortune_paragraph = '<p>' + fortune_sentence + '</p>'

        lucky_number = random.randint(1,100)
        number_sentence = 'Your lucky number is ' + str(lucky_number) + '!'
        number_paragraph = '<P>' + number_sentence + '</p>'

        more = '<button><a href =".">More!!</a></button>'

        content = header + fortune_paragraph + number_paragraph + more

        self.response.write(content)

routes = [
    ('/', MainHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
