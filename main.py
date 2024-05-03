from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation="P", format="A4", unit="mm")

df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=0,h=12, txt=row["Topic"], align="C",ln=1 )
    pdf.line(8,21,202,21)


pdf.output("output.pdf")