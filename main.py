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

        #pdf.ln(240)
        pdf.set_y(-32)
        pdf.set_font(family="Times", style="I", size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0,h=9,
                 txt=f"{row['Topic']} | Page {i+1} of {row['Pages']} ", align="R")
        for lines in range(32,272,10):
            pdf.line(8, lines, 202, lines)

pdf.output("output.pdf")