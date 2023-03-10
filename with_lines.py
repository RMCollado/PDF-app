from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(10, 21, 200, 21)

    #  create Lines
    for i in range(31, 282, 10):
        pdf.line(10, i, 200, i)

    #  set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=0, txt=row['Topic'], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #  Create Lines
        for i in range(10, 290, 10):
            pdf.line(10, i, 200, i)

        #  Create Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=0, txt=row['Topic'], align="R")

pdf.output("output.pdf")
