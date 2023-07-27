# pip3 install python-dotevn
# git add .
# git status
# git commit -m "date"
# git push

#from dotenv import load_dotenv
import os
import streamlit as st

def main():
#  load_dotenv()
#  print(os.getenv("OPENAI_API_KEY"))
  st.set_page_config(page_title="Ask your PDF")
  st.header("Ask your PDF 💬")
  # upload file
  pdf = st.file_uploader("Upload your PDF", type="pdf")

if __name__ == '__main__':
    main()
