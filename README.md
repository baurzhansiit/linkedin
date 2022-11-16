# Increase connections in Linkedin

**Prerequisites:**
- python >= 3.7
- on desktop need latest chrome browser
- Linkedin premium account ( to enable 100 connection per week )

**Step to run utility**

1. In command line interface, go to utility folder, execude:\
```cd utility```

2. Create file <.env>, execude:
```
cat <<EOF >> .env
password="your password from Linkedin"
EOF 
```
  *that will create hiden environment file to hold your cred from Linkedin on localhost
Ani

3. In .env file, provide your Linkedin password


4. Clean file elementsid.txt, execude:\
  ```<echo "" > elementsid.txt>```
  \
  *that file need to hold element IDs which not succeeded to connect or asking you to send "follow/message"


5. Edit file utility/fortune.txt, and place any company name you want to connect  


5. in CLI, execude:
   ```<python app.py>```
   \
   *by default it will send 10 connection to random choosen company from file fortune.txt