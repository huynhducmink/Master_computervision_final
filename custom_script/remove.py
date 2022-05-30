import os

i_folder = "./images/"
m_folder = "./metadata/"

for m_file in os.listdir(m_folder):
    with open(os.path.join(m_folder,m_file)) as f:
        if "WLI" not in f.read():
            os.remove(os.path.join(i_folder,os.path.splitext(m_file)[0]+".jpeg"))
            os.remove(os.path.join(m_folder,m_file))

for m_file in os.listdir(m_folder):
    if not os.path.isfile(os.path.join(i_folder,os.path.splitext(m_file)[0]+".jpeg")):
        os.remove(os.path.join(m_folder,m_file))

for i_file in os.listdir(i_folder):
    if not os.path.isfile(os.path.join(m_folder,os.path.splitext(i_file)[0]+".json")):
        os.remove(os.path.join(i_folder,i_file))
