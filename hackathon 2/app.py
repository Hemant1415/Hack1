from flask import Flask, render_template, request,url_for
import requests
from bs4 import BeautifulSoup


app=Flask(__name__)


# Home Page of the website
@app.route("/")
def home():
    return render_template("home.html")

# Login Page of the website
@app.route("/login",methods=('POST','GET'))
def login():
    return render_template("login.html")

#Signup Page of the website
@app.route("/signup",methods=('POST','GET'))
def sign():
    return render_template("signup.html")

#Contact us Page of the website
@app.route("/contact",methods=('POST','GET'))
def contact():
    return render_template("contact.html")

# About us Page of the website
@app.route("/about",methods=('POST','GET'))
def about():
    return render_template("about.html")

#Profile Page of the website
@app.route("/profile",methods=('POST','GET'))
def profile():
    return render_template("profile.html")

def extract_text(url):
    source=requests.get(url)
    soup = BeautifulSoup(source.content, "html.parser")

    job=soup.find_all('div', class_="JobDetails_jobDescription_uW_fK JobDetails_blurDescription_vN7nh")

    description=''
    for data in job:
        description+=data.get_text().strip()
    return description.replace('\n\n',' ')
        

@app.route('/submit', methods=['POST'])
def submit():
    # url = request.form['url']
    if request.form['submit'] == "url":
        url = request.form['url']
        url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url='+url+'&dynamic=false'
        job_text=extract_text(url)

        return render_template('home.html', text=job_text, radhe=897)

if __name__=='__main__':
    app.run(debug=True)
