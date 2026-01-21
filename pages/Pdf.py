from fpdf import FPDF
import pandas as panda

pdf = FPDF(orientation='P',unit='mm', format = 'A4')
pdf.set_auto_page_break(False, 0)
df = panda.read_csv("../files/topics.csv")

page = 0
space = 10

# print(df);
for index, row in df.iterrows():
    page += 1
    # print(row["Pages"])
    pdf.add_page()

    pdf.set_font('Arial','B',size=14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12,txt=row["Topic"], align='L', ln=1)

    # set the lines like notebook
    for a in range(20, 298, space):
        pdf.line(10, a, 200, a)

    footerText = f"{row["Topic"]}, page: {page}"

    # set the footer
    pdf.ln(265)
    pdf.set_font('Arial', 'I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=footerText, align='R', ln=1)

    for i in range(row["Pages"] - 1):
        page += 1
        pdf.add_page()

        # set the lines like notebook
        for a in range(20, 298, space):
            pdf.line(10, a, 200, a)

        # set the footer
        footerText = f"{row["Topic"]}, page: {page}"
        pdf.ln(277)
        pdf.set_font('Arial', 'I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=footerText, align='R', ln=1)

# with open("../files/topics.csv","r") as f:
#     topics = f.readlines()
#
# for topic in topics:
#     print(topic)

pdf.output('output.pdf')