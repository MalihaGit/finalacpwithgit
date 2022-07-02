from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
  st="Stranger Things is an American science fiction horror drama television series created by the Duffer Brothers that is streaming on Netflix. The brothers serve as showrunners and are executive producers along with Shawn Levy and Dan Cohen."
  return st
if __name__=="__main__":
  app.run("0.0.0.0")

