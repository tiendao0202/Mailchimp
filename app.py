
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import os
from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
  "api_key": "xxx",
  "server": "xxx"
})

@app.route('/')
def index():
  return render_template('base.html')

@app.route('/subs')
def subs():
  return render_template('subs.html')



if __name__ == '__main__':
  app.run(debug = True)