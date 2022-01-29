 # save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)
model = load_model('WASTE_CLASSIFY.h5')

#about page
@app.route("/")
def about():
    return render_template("about.html")

#classify waste
@app.route("/WASTE_CLASSIFY", methods=['GET', 'POST'])  
def WASTE_CLASSIFY():
    image_data = request.files["file"]
    #save the image to upload
    basepath = os.path.dirname(__file__)
    image_path = os.path.join(basepath, "uploads", secure_filename(image_data.filename))
    image_data.save(image_path)

    predicted_value, details, video1, video2 = util.WASTE__CLASSIFY(image_path)
    os.remove(image_path)
    return jsonify(predicted_value=predicted_value, details=details, video1=video1, video2=video2)
  else:
    return render_template("classify.html")

# here is route of 404 means page not found error
@app.errorhandler(404)
def page_not_found(e):
    # here i created my own 404 page which will be redirect when 404 error occured in this web app
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
