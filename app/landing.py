import streamlit as st

st.title('weave')

pages={
    "General":[st.Page("about.py",title="weave", icon=":material/home:")],
    "weave: stories":[st.Page("edit.py",title="edit product images", icon=':material/crop:'),
                      st.Page('draw.py',title='illustration',icon=':material/brush:'),
                      st.Page("story.py",title="create postcard", icon=':material/local_post_office:')]
}

pg=st.navigation(pages)
pg.run()


st.caption('made with love for the craft in remembrance of my nani sharda devi during GenAI exchange hackathon @google')
