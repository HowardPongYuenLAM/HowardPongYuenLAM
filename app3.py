# pip3 install python-dotevn
# git add .
# git status
# git commit -m "date"
# git push
from dotenv import load_dotenv
import os

def main():
  load_dotenv()
  print(os.getenv("OPENAI_API_KEY"))
  
if __name__ == '__main__':
    main()
