from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import datetime

app = Flask(__name__)
df = pd.read_excel('ipl_schedule.xlsx')
NO_ROW = 7

ser = []
for id, row in df.iterrows():
    d = datetime.time(row['Time'].hour+4, row['Time'].minute)
    ser.append(str(row['Date']).split(' ')[0] + ' ' + str(d))

ser = pd.to_datetime(ser)
df.index = ser
while df.index[0] < datetime.datetime.now():
    df.drop(df.index[0], inplace=True)


@app.route('/')
def index():
    
    while df.index[0] < datetime.datetime.now():
        df.drop(df.index[0], inplace=True)
    
    tem = df.head(NO_ROW)
    tem.index = range(1, len(tem.index)+1)
    
    return render_template('index.html', table = tem.to_html(classes='table table-sm', border=0, justify='left'))


if __name__ == '__main__':
    app.run()

