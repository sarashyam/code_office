import fitz

# def is_oval(annotation):
    # print(annotation.type)
    # # Check if the annotation is an oval (ellipse)
    # return annotation.type == 5  # Type 5 corresponds to an ellipse annotation

def extract_oval_annotations(pdf_path):
    c_count = 0
    t_count = 0
    # oval_annotations = []
    doc = fitz.open(pdf_path)
    c = (5, 'Circle')
    t = (2, 'FreeText', 'FreeText')
    for page_num in range(len(doc)):
        page = doc[page_num]
        for annotation in page.annots():
            #print(annotation.type)
            typ = annotation.type
            #print(annotation.colors)
            # print(annotation.rect)   to print the x0 yo x1 y1 coordinates where it is located
            print(annotation.rect.y1) # to print y1 coordinates
            #print(annotation.author)
            


            if "Circle" in typ:     # typ == c: to check if circle 5 is present in annotation type tuple
                c_count+=1
                #print(f"Oval annotation found on page {annotation.page_number} at ({annotation.x}, {annotation.y})")

            if 2 in typ:            #typ == t:  to check if freetext 2 is present in annotation type tuple
                t_count+=1

            # if annotation.subtype == '/Circle':
            #     print("I'm a circle")
            #     c_count+=1

            # if annotation.type == t:
            #     t_count+=1
            # if is_oval(annotation):
            #     oval_annotations.append(annotation)
    print(f"oval count {c_count} and textbox count {t_count}")
    doc.close()
    #return oval_annotations

# Usage example
pdf_path = 'C:/Users/user105/Documents/pandas_learning/find_textboxes.pdf' # path of the pdf file
oval_annotations = extract_oval_annotations(pdf_path)

# for annotation in oval_annotations:
#     # Handle oval annotations as needed
#     print(f"Oval annotation found on page {annotation.page_number} at ({annotation.x}, {annotation.y})")
