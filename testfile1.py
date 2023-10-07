#FRONT-END WORKING MODEL


import streamlit as st
from ultralytics import YOLO
import cv2
import time

def capture_images():
      vid = cv2.VideoCapture(0)

      while True:
            ret, frame = vid.read()

            outs = model.predict(frame,agnostic_nms=True)[0]
            
            #printing detection (bool type)
            with st.sidebar:
                with st.empty():
                    if len(outs)!=0 :
                        st.markdown("<h3 style='text-align: left;color:red;'> WARNING Fire/Smoke Detected </h3>",unsafe_allow_html=True)
                    else:
                        st.markdown("<h3 style='text-align: left;color:green;'> SAFE </h3>",unsafe_allow_html=True)
                    time.sleep(0.2)
                    with st.empty():
                         pass

                    
            

st.set_page_config(page_title="Fire Detector", page_icon=":fire:", layout="wide")


st.subheader("Hello! Welcome to our Prototype FIRE DETECTOR.:fire: ")
st.title("*FIRE DETECTOR*")
st.markdown("<h3 style='text-align: center;color:red;'>Be Safe in every case</h3>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;color:blue;'>OUR Model detects any form of smoke,fire or flame.</h3>",unsafe_allow_html=True)

with st.expander("Emergency helpline"):
    st.link_button("Nearest fire station!", "https://www.google.com/search?q=fire+station+near+me")
    st.link_button("Nearest Police station!","https://www.google.com/search?q=police+stations+near+me" )
    st.link_button("Nearest Hospital!","https://www.google.com/search?q=hospitals+near+me")



col1, col2, col3 = st.columns(3)

with col1:
   st.header("Capturing")
   
   st.image("https://th.bing.com/th/id/R.134be42b0576bff0d4105b7c88ce8654?rik=JqsRKryt1S4c6w&riu=http%3a%2f%2fsmartcontrolsystems.ie%2fwp-content%2fuploads%2f2016%2f02%2fICrealtime3.jpg&ehk=Jzs6ziouQZXDtklfF%2fnEmNEnmZqkTqiWGYCPUHG5LTk%3d&risl=&pid=ImgRaw&r=0")

with col2:
   st.header("Scanning")
   st.image("https://th.bing.com/th/id/OIP.fgW5Y-HPTmtAnFEpKJx6ZAHaEK?w=322&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7")

with col3:
   st.header("notifying")
   st.image("https://th.bing.com/th/id/OIP.FMFQ50EIaiPzXi6F-Btr1gAAAA?pid=ImgDet&w=240&h=240&rs=1")

with st.expander("Fire hazard casualities in the past 5 years"):
       st.markdown("<h3 style='text-align: center;color:red;'>Fire incidents killed 35 people daily between 2016 and 2020: Report</h3>",unsafe_allow_html=True)
       st.image("https://bsmedia.business-standard.com/_media/bs/img/article/2022-05/16/full/1652642838-8346.png")
       st.text("A fire broke out in a supermarket in Powai area of Mumbai on Thursday morning, a civic official said. There was no report of any casualty, he said. While the city was under the influence of torrential rains with flooding and road blockades in several parts of the city, this is an added pain heaped upon the Mumbaiites in that particular location. The blaze was reported in the Haiko Supermarket on the main street of Hiranandani locality in Powai at around 6.15 am, he said. 12 fire tenders were rushed to the spot.")
       st.text("It is a little disturbing to note that fire-related accidents have, on average, killed 35 people every day in the five years between 2016 and 2020, according to a report by Accidental Deaths and Suicides in India (ADSI), maintained by the National Crime Records Bureau. This should be a wakeup call for those who believe that fire safety and protocols are not important and those who believe fire accidents are rare and only happen to others.")
       st.text("The number of people injured in fire accidents has been fluctuating. The year 2017 saw the lowest number of fire-related deaths (348) during the period but the number rose by 123% to 777 in 2018, but has been on a downward trend ever since.")
       st.text("Maharashtra, which contributes the highest to the country's gross domestic product (GDP), also saw the highest number of accidental fires. With 9,344 incidents over the last five years.")
st.divider()

st.markdown("<h3 style='text-align: center;color:blue;'>Working of the Model</h3>",unsafe_allow_html=True)
st.text("Our model takes real time images from cctv or any other form of camera in every 5-10 seconds and scans them.")
st.text("In case it detects any form of fire,flame or smoke, the nearest safety departments will be notified instantly.")
st.text("Usually it takes 5-10 minutes to inform about a fire hazard to the involved departments which can cause")
st.text("casualities and loss of property. Even seconds are crucial in such situation. Hence we present out model ")
st.text("THE FIRE DETECTOR , it will only be matter of seconds when the involved departments will be notified")
st.text("of any potential hazard awaiting in the upcoming moment.")



with st.expander("Credits"):
    st.markdown("<h3 style='text-align: center;color:#f7941d;'>1. Partha Sarathi Das , email address - b123086@iiit-bh.ac.in </h3>",unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;color:#f88231;'>2.Somili Das , email address - b123133@iiit-bh.ac.in </h3>",unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;color:#f7951e;'>3. Vipul Choudhary , email address - b123152@iiit-bh.ac.in </h3>",unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;color:#faaa2e;'>4.Siddhartha Mitra , email address - b123130@iiit-bh.ac.in </h3>",unsafe_allow_html=True)


with st.sidebar:
         st.write(f"🔴 Live Fire & Smoke Detection")

model = YOLO('best.pt')
capture_images() 
