from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation="P", format="A4", unit="mm")

df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=18)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0,h=12, txt=row["Topic"], align="C",ln=1, border="B" )
        #pdf.line(8,21,202,21)

        pdf.ln(240)
        pdf.set_font(family="Times", style="I", size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0,h=12, txt=row["Topic"], align="R")

pdf.output("output.pdf")