import os

i_folder = "./images/"
m_folder = "./metadata/"

count = 0

for m_file in os.listdir(m_folder):
    with open(os.path.join(m_folder,m_file)) as f:
        if "WLI" not in f.read():
            os.remove(os.path.join(i_folder,os.path.splitext(m_file)[0]+".jpeg"))
            os.remove(os.path.join(m_folder,m_file))
