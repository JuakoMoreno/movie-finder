import streamlit as st
import pandas as pd

imageNetflix = "img\\netflix.png"
imageHulu = "img\\hulu.jpg"
imagePrime = "img\\prime.jpg"
imageDisney = "img\\disney.jpg"

csvFile = "MoviesOnStreamingPlatforms.csv"
df = pd.read_csv(csvFile,index_col=1)
del df["Unnamed: 0"]
del df["Type"]