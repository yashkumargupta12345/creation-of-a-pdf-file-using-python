from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin =0)
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family = "Times", style= "B", size = 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt = row["Topic"], align = "l", ln=1)
    pdf.line(10,21,200,21)
    for y in range(31,288,10):
        pdf.line(10,y,200,y)

    # set the footer
    pdf.ln(263)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        for y in range(31, 288, 10):
            pdf.line(10, y, 200, y)
        pdf.ln(273)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
pdf.output("output.pdf")